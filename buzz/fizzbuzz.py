
def fizzbuzz(min, max):
    fizzbuzz = []
    for number in range(min, max+1):
        isFizz = number % 3
        isBuzz = number % 5

        result = ''
        if isFizz == 0:
            result += 'Fizz'
        if isBuzz == 0:
            result += 'Buzz'

        fizzbuzz.append(result if result else number)
    return fizzbuzz


if __name__ == "__main__":
    print(fizzbuzz(0, 100))