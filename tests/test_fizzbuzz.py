from buzz import fizzbuzz


def test_fizzbuzz():
    result = fizzbuzz.fizzbuzz(1, 30)
    assert result[1] == 1
    assert result[3] == 'Fizz'
    assert result[5] == 'Buzz'
    assert result[15] == 'FizzBuzz'
