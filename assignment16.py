# Assignment-16 (Python - Fizz - Buzz Numbers)

numbers = list(range(1, 101))

for i in numbers :

    """first condition must be before below conditions to be able to reach out the numbers that are multiple of both 3 and 5 """

    if i % 3 == 0 and i % 5 == 0 :   # or i % 15 == 0
        numbers[numbers.index(i)] = 'FizzBuzz'

    elif i % 3 == 0 :
      numbers[numbers.index(i)] = 'Fizz'

    elif i % 5 == 0 :
      numbers[numbers.index(i)] = 'Buzz'
    else :
        continue

print(numbers)

[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
