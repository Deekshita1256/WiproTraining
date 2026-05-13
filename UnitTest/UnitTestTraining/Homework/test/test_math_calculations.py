import unittest
from Homework.src.math_calculations import add, subtract, divide


# 1. Basic Test Case
class TestMath(unittest.TestCase):
    def test_add_simple(self):
        self.assertEqual(add(2, 3), 5)


# 2. Setup and Teardown
class TestList(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(len(self.data), 3)


# 3. Multiple Assertions
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())


# 4. Exception Testing
class TestExceptions(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


# 5. Test Suite Execution Classes
class TestAdd(unittest.TestCase):
    def test_run_add(self):
        self.assertEqual(add(10, 5), 15)


class TestSubtract(unittest.TestCase):
    def test_run_subtract(self):
        self.assertEqual(subtract(10, 5), 5)


if __name__ == "__main__":
    # Create the Test Suite
    suite = unittest.TestSuite()

    # Add specific classes to the suite
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    # Run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
