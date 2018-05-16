import os
import pyphptree

def test_file(fn):
    with open(fn, encoding='utf8') as f:
        lines = f.read().splitlines()
        print('\nHeaders in: '+fn)
        for item in pyphptree.get_headers(fn, lines):
            print('  ', item)


dir = os.path.join(os.path.dirname(__file__), 'testfiles')
v = sorted(os.listdir(dir))
v = [os.path.join(dir, s) for s in v if s.endswith('.php')]
for fn in v:
    test_file(fn)
