import unittest
from bpipe import pipe, cat, echo


class TestGenerators(unittest.TestCase):
    def test_range(self):
        result = list(pipe(range(1, 5)))
        self.assertEqual(result, [1, 2, 3, 4])
    def test_echo(self):
        result = list(echo("HelloWorld"))
        self.assertEqual(result, ["HelloWorld"])
    def test_cat(self):
        result = list(cat("tests/fileinput.txt"))
        self.assertEqual(result, ["1", "2", "3", "4", "5"])


if __name__ == '__main__':
    unittest.main()
