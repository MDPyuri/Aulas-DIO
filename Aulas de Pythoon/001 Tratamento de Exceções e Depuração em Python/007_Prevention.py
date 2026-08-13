import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()