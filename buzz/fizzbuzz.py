
def fizzbuzz(min, max):
    result = []
    for number in range(min, max+1):
        item = ''
        if number % 3 == 0:
            item += 'Fizz'
        if number % 5 == 0:
            item += 'Buzz'
        result.append(result if result else number)
    return result


if __name__ == "__main__":
    print(fizzbuzz(0, 100))
