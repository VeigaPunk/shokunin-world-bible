#!/usr/bin/env python3
import json, sys

d = json.load(open(sys.argv[1]))
print('run_at', d['run_at'])
for f in d['files']:
    print('==', f['file'], '| self-sha256[:8]=', f['sha256_8'], '| pins=', len(f['pins']))
    for p in f['pins']:
        deliv = [m for m in p['delivered_match'] if not m.startswith('.ufo/')]
        scratch = len(p['delivered_match']) - len(deliv)
        tag = ('DELIVERED:' + ','.join(deliv)) if deliv else ('scratch-only(x%d)' % scratch if scratch else 'NO-MATCH-ANYWHERE')
        print('  L%-3d %-64s w%-2d %-8s %s' % (p['line'], p['token'], p['width'], p['kind'], tag))
