# 1. Basic Test Function
    # Write a pytest test function that checks whether the sum of two numbers (3 and 5) equals 8.

class Arithmetics:
    def add(self, n1, n2):
        return n1 + n2

# 2. Assertion Failure
    # Create a pytest test that intentionally fails by asserting that "hello".upper() equals "hello".

    def to_uppercase(self, text: str) -> str:
        return text.upper()

# 3. Fixture Usage
    # Define a pytest fixture that returns a list of numbers [1, 2, 3]. Write a test that uses this fixture to verify the list length is 3.

    def number_list(self):
        return [1, 2, 3]

# 4. Parameterized Test
    # Use @pytest.mark.parametrize to test a function square(x) for inputs 2, 3, 4 and expected outputs 4, 9, 16.

    def square(self, n1):
        return n1 ** 2

# 5. Exception Handling
    # Write a pytest test that verifies a ZeroDivisionError is raised when dividing by zero using pytest.raises.

    def div(self, n1, n2):
        return n1 / n2