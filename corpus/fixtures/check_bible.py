#!/usr/bin/env python3
"""Validate a small cited fictional-world bible; report, never resolve, contradictions."""
import argparse
import json
from pathlib import Path

KINDS = {'character', 'place', 'faction', 'item'}
FIELDS = {
    'sources': {'id': str, 'title': str, 'kind': str, 'reliability_note': str},
    'entities': {'id': str, 'kind': str, 'name': str, 'first_appearance': str, 'claims': list},
    'relations': {'from': str, 'to': str, 'type': str, 'source_id': str},
    'timeline': {'id': str, 'tick': int, 'entity_id': str, 'place_id': str,
                 'depends_on': list, 'description': str, 'source_id': str},
}


def check(directory):
    errors = []
    data = {}
    for section, fields in FIELDS.items():
        path = directory / (section + '.json')
        try:
            rows = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f'{path.name}: cannot load JSON: {exc}')
            rows = []
        if not isinstance(rows, list):
            errors.append(f'{path.name}: expected array')
            rows = []
        data[section] = []
        for index, row in enumerate(rows):
            location = f'{section}[{index}]'
            if not isinstance(row, dict):
                errors.append(f'{location}: expected object')
                continue
            valid = True
            for field, expected in fields.items():
                if field not in row or type(row[field]) is not expected or (expected is str and not row[field].strip()):
                    errors.append(f'{location}.{field}: required nonempty {expected.__name__}')
                    valid = False
            if valid:
                data[section].append((location, row))

    def index(section):
        result = {}
        for location, row in data[section]:
            if row['id'] in result:
                errors.append(f'{location}.id: duplicate {section} id {row["id"]!r}')
            result[row['id']] = row
        return result

    sources = index('sources')
    entities = index('entities')
    events = index('timeline')

    def source(source_id, location):
        if source_id not in sources:
            errors.append(f'{location}: unknown in-world source {source_id!r}')

    for location, row in data['entities']:
        if row['kind'] not in KINDS:
            errors.append(f'{location}.kind: unknown kind {row["kind"]!r}')
        source(row['first_appearance'], location + '.first_appearance')
        for i, claim in enumerate(row['claims']):
            label = f'{location}.claims[{i}]'
            if not isinstance(claim, dict) or not isinstance(claim.get('statement'), str) or not claim['statement'].strip() or not isinstance(claim.get('source_id'), str):
                errors.append(f'{label}: expected nonempty statement and source_id')
            else:
                source(claim['source_id'], label + '.source_id')

    for location, row in data['relations']:
        for endpoint in ('from', 'to'):
            if row[endpoint] not in entities:
                errors.append(f'{location}.{endpoint}: dangling entity {row[endpoint]!r}')
        source(row['source_id'], location + '.source_id')

    # Only distinct, resolvable faction pairs participate; self-edges are out of scope.
    entity_id_counts = {}
    for _, entity in data['entities']:
        entity_id_counts[entity['id']] = entity_id_counts.get(entity['id'], 0) + 1
    allied = [row for _, row in data['relations'] if row['type'] == 'allied_with']
    for location, row in data['relations']:
        left, right = row['from'], row['to']
        if row['type'] != 'allied_with' or left == right:
            continue
        if (left not in entities or right not in entities
                or entity_id_counts[left] != 1 or entity_id_counts[right] != 1
                or entities[left]['kind'] != 'faction' or entities[right]['kind'] != 'faction'):
            continue
        reciprocal = any(
            candidate['from'] == right and candidate['to'] == left
            and candidate['type'] == 'allied_with'
            and candidate['source_id'] in sources
            for candidate in allied
        )
        if not reciprocal:
            errors.append(f'{location}: allied_with faction relation {left!r} -> {right!r} lacks a sourced reciprocal relation')

    occupied = {}
    for location, row in data['timeline']:
        for field in ('entity_id', 'place_id'):
            if row[field] not in entities:
                errors.append(f'{location}.{field}: dangling entity {row[field]!r}')
        if row['place_id'] in entities and entities[row['place_id']]['kind'] != 'place':
            errors.append(f'{location}.place_id: not a place {row["place_id"]!r}')
        source(row['source_id'], location + '.source_id')
        if row['tick'] < 0:
            errors.append(f'{location}.tick: must be nonnegative')
        if not all(isinstance(dep, str) for dep in row['depends_on']):
            errors.append(f'{location}.depends_on: expected event-id strings')
            continue
        slot = (row['entity_id'], row['tick'])
        if slot in occupied and occupied[slot][1] != row['place_id']:
            previous, prior_place = occupied[slot]
            errors.append(f'{location}: double-booked {row["entity_id"]!r} at tick {row["tick"]} in {previous} ({prior_place!r}) and {row["place_id"]!r}')
        else:
            occupied[slot] = (location, row['place_id'])
        for dep in row['depends_on']:
            if dep not in events:
                errors.append(f'{location}.depends_on: unknown event {dep!r}')
            elif events[dep]['tick'] >= row['tick']:
                errors.append(f'{location}.depends_on: timeline inversion {dep!r} tick {events[dep]["tick"]} not before {row["id"]!r} tick {row["tick"]}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bible', type=Path, help='directory with sources, entities, relations, timeline JSON arrays')
    args = parser.parse_args()
    violations = check(args.bible)
    for violation in violations:
        print('VIOLATION:', violation)
    if violations:
        print(f'{len(violations)} violation(s); no canon changed')
        raise SystemExit(1)
    print('CLEAN: schema, citations, relations, timeline; 0 violations')
