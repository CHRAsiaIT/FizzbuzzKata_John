from fizzbuzz import Fizzbuzz
def test_one():
    assert Fizzbuzz.value_of(1) == 1

def test_two():
    assert Fizzbuzz.value_of(2) == 2

def test_three():
    assert Fizzbuzz.value_of(3) == "Fizz"

def test_five():
    assert Fizzbuzz.value_of(5) == "Buzz"