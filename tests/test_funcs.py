import unittest
from bpipe import Pipe, map_to, flat_map, flatten

class TestGenerators(unittest.TestCase):
    def test_map(self):
        param = [1, 2, 3, 4, 5]
        trans = lambda x: x+3
        p1 = Pipe(param).map(trans)
        p2 = Pipe(param) | map_to(trans)
        self.assertEqual(list(p1), list(p2))

    def test_flatten(self):
        param = [[1, 2], [3, 4]]
        result = [1, 2, 3, 4]
        p1 = Pipe(param).flatten()
        p2 = Pipe(param) | flatten()
        r1 = list(p1)
        r2 = list(p2)
        self.assertEqual(r1, result)
        self.assertEqual(r2, result)
        self.assertEqual(r1, r2)

    def test_flatmap(self):
        param = [[1, 2], [3, 4]]
        result = [2, 3, 4, 5]
        trans = lambda x: x+1
        p1 = Pipe(param).flat_map(trans)
        p2 = Pipe(param) | flat_map(trans)
        r1 = list(p1)
        r2 = list(p2)
        self.assertEqual(r1, result)
        self.assertEqual(r2, result)
        self.assertEqual(r1, r2)

if __name__ == '__main__':
    unittest.main()
