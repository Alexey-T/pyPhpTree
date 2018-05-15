import os
import pyphptree

dir = os.path.dirname(__file__)
fn = os.path.join(dir, 'testfiles', 'a.php')
with open(fn, encoding='utf8') as f:
    lines = f.read().splitlines()
    print(pyphptree.get_headers(lines))
