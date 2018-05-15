import os
import pyphptree

dir = os.path.dirname(__file__)
fn1 = os.path.join(dir, 'testfiles', 'a.php')
fn2 = os.path.join(dir, 'testfiles', 'c.php')

def test_file(fn):
    with open(fn, encoding='utf8') as f:
        lines = f.read().splitlines()
        print('Headers in: '+fn)
        print(list(pyphptree.get_headers(lines)))

test_file(fn1)
test_file(fn2)
