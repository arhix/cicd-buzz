from buzz import fizzbuzz


def test_fizzbuzz():
    result = fizzbuzz.fizzbuzz(0, 5)
    assert result[0] == 'FizzBuzz'
    assert result[1] == 1
    assert result[3] == 'Fizz'
    assert result[5] == 'Buzz'
