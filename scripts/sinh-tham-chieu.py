"""Generate docs/settings-reference.md from the theme's schema.json and config.json.

Run from the repo root with the theme checked out next to it:

    python scripts/sinh-tham-chieu.py ../bc-nexus-sport-theme

Re-run after every theme release so labels and defaults never drift.
"""
import io
import json
import os
import sys

THEME = sys.argv[1] if len(sys.argv) > 1 else '../bc-nexus-sport-theme'
doc = lambda p: json.load(io.open(os.path.join(THEME, p), encoding='utf-8'))
schema = doc('schema.json')
tr = doc('schemaTranslations.json')
cfg = doc('config.json')
mac_dinh = cfg['settings']
bien_the = {v['name']: v['settings'] for v in cfg['variations']}


def nhan(k):
    if isinstance(k, str) and k in tr:
        return tr[k].get('default', k)
    return k or ''


def gia_tri(v):
    if v is True:
        return 'On'
    if v is False:
        return 'Off'
    if v in ('', None):
        return '*(empty)*'
    s = str(v).replace('|', '\\|')
    return '`%s`' % s if len(s) < 40 else '`%s…`' % s[:37]


def chon(x, v):
    for o in x.get('options', []):
        if str(o.get('value')) == str(v):
            return nhan(o.get('label'))
    return None


dong = ['# Settings reference', '',
        'Every setting in Theme Styles, grouped as they appear there, with the value',
        'the **Nexus Track** variation ships with. Where another variation differs,',
        'its value is listed in the last column.', '',
        'Colour values are hex codes; in Theme Styles each one opens a colour picker.', '']
for g in schema:
    dong += ['## ' + nhan(g['name']), '']
    bang = []
    tieu_de = None
    for x in g['settings']:
        if x['type'] == 'heading':
            tieu_de = nhan(x.get('content'))
            continue
        if x['type'] == 'paragraph' or 'id' not in x:
            continue
        v = mac_dinh.get(x['id'])
        hien = chon(x, v) or gia_tri(v)
        if x['type'] == 'color':
            hien = '`%s`' % v if v else '*(empty)*'
        khac = ['%s: %s' % (n.split()[-1], chon(x, s[x['id']]) or gia_tri(s[x['id']]))
                for n, s in bien_the.items() if x['id'] in s and s[x['id']] != v]
        bang.append((tieu_de or '', nhan(x.get('label')) or x['id'], hien, ', '.join(khac)))
    if not bang:
        continue
    dong += ['| Section | Setting | Default | Other variations |', '|---|---|---|---|']
    truoc = None
    for t, l, h, k in bang:
        dong.append('| %s | %s | %s | %s |' % (t if t != truoc else '', l.replace('|', '\\|'), h, k))
        truoc = t
    dong.append('')

ra = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'settings-reference.md')
io.open(ra, 'w', encoding='utf-8', newline='\n').write('\n'.join(dong))
print('wrote', ra, len(dong), 'lines')
