import kata

def test_empty_string():
    assert kata.Add("") == 0

def test_single_digit():
    assert kata.Add("1") == 1