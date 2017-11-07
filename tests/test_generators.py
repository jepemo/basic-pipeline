import unittest
from bpipe import pipe


class TestGenerators(unittest.TestCase):
    def test_range(self):
        result = pipe(range(1, 5)).get()
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
