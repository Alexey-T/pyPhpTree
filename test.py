import os
import pyphptree

dir = os.path.dirname(__file__)
fn = os.path.join(dir, 'testfiles', 'c.php')
with open(fn, encoding='utf8') as f:
    lines = f.read().splitlines()
    res = list(pyphptree.get_headers(lines))
    print('headers:\n', res)
