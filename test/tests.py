import unittest


class TestMain(unittest.TestCase):
    def test_hello(self):
        print("Hello, world!")
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
    