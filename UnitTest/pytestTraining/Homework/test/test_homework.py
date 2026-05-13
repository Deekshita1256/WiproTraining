# 1. Basic Test Function
    # Write a pytest test function that checks whether the sum of two numbers (3 and 5) equals 8.

import pytest
from Homework.src.homework import Arithmetics


class TestArithmetics:
    @pytest.fixture(autouse=True)
    def setup(self):
        # create an instance of your Arithmetics class
        self.arth = Arithmetics()


    def test_add(self):
        res = self.arth.add(10, 5)
        assert res == 15, 'Addition error'

# 2. Assertion Failure
    # Create a pytest test that intentionally fails by asserting that "hello".upper() equals "hello".

    def test_uppercase_failure(self):
        # This will fail because "HELLO" != "hello"
        res = self.arth.to_uppercase('hello')
        assert res == "hello", 'Uppercase Error'

# 3. Fixture Usage
    # Define a pytest fixture that returns a list of numbers [1, 2, 3]. Write a test that uses this fixture to verify the list length is 3.

    def test_number_list(self):
        res = len(self.arth.number_list())
        assert res == 3, 'List length error'

# 4. Parameterized Test
    # Use @pytest.mark.parametrize to test a function square(x) for inputs 2, 3, 4 and expected outputs 4, 9, 16.

    @pytest.mark.parametrize("n1, exval",
                             [(2, 4), (3, 9), (4, 16)])
    def test_square(self, n1, exval):
        res = self.arth.square(n1)
        assert res == exval, 'Squaring Error'

# 5. Exception Handling
    # Write a pytest test that verifies a ZeroDivisionError is raised when dividing by zero using pytest.raises.

    def test_div(self):
        with pytest.raises(ZeroDivisionError):
            self.arth.div(19, 0)

