def test_min_window_substring():
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC", "Test case 1 failed"
    assert min_window_substring("a", "aa") == "", "Test case 2 failed"
    assert min_window_substring("this is a test string", "tist") == "t stri", "Test case 3 failed"
    assert min_window_substring("geeksforgeeks", "ork") == "ksfor", "Test case 4 failed"
    print("All test cases passed!")

# Run the test function
test_min_window_substring()
