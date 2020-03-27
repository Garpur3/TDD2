import kata

def test_empty_string():
    assert kata.Add("") == 0

def test_single_digit():
    assert kata.Add("1") == 1

def test_two_digits():
    assert kata.Add("1,2") == 3

def test_multiple_numbers():
    assert kata.Add("1,2,3,4,5") == 15

def test_with_newline():
    assert kata.Add("1\n2,3") == 6

def test_greater_than_1000():
    assert kata.Add("1001,2") == 2