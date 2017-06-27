
def fizzbuzz(min, max):
    result = []
    for number in range(min, max+1):
        item = ''
        if number % 3 == 0:
            item += 'Fizz'
        if number % 5 == 0:
            item += 'Buzz'
        result.append(item if item else number)
    return result
