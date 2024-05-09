import pytest
from mycode import sum_of_multiples  # Ensure this import matches the actual path and function

def test_sum_of_multiples():
    assert sum_of_multiples(20, 5) == 50, "Test case 1 failed"
    assert sum_of_multiples(15, 3) == 45, "Test case 2 failed"
    assert sum_of_multiples(10, 2) == 20, "Test case 3 failed"
    assert sum_of_multiples(30, 7) == 7 + 14 + 21 + 28, "Test case 4 failed"
    assert sum_of_multiples(50, 10) == 10 + 20 + 30 + 40 + 50, "Test case 5 failed"
    print("All test cases passed!")

# Run the test function
test_sum_of_multiples()
