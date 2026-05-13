import pytest
import os


# --- 1. The Basic Assertion ---
def test_math_operations():
    # Verify multiplication
    assert 15 * 3 == 45
    # Verify string membership
    assert "pytest" in "Learning pytest is fun"


# --- 2. Using Fixtures for Setup ---
@pytest.fixture
def sample_dict():
    return {"name": "Alice", "role": "Dev"}


def test_dict_keys(sample_dict):
    assert "role" in sample_dict
    assert sample_dict["name"] == "Alice"


# --- 3. Handling Exceptions ---
def get_element(my_list, index):
    return my_list[index]


def test_index_error():
    with pytest.raises(IndexError):
        get_element([1, 2, 3], 10)


# --- 4. Parameterized Testing ---
@pytest.mark.parametrize("number", [2, 10, 22])
def test_is_even(number):
    assert number % 2 == 0


# --- 5. Cleaning Up with Fixture Yields ---
@pytest.fixture
def temp_file():
    # Setup: Create the file
    filename = "test.txt"
    with open(filename, "w") as f:
        f.write("Hello World")

    yield filename  # This is where the test runs

    # Teardown: Delete the file
    if os.path.exists(filename):
        os.remove(filename)


def test_file_content(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "Hello World"
