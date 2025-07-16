# Program for FizzBuzz if divided by 3, print Fizz, by 5, print Buzz, by 3 & 5 both, print FizzBuzz
for number in range(1,16):
    if number%3 == 0 and number%5 == 0:
        print("Fizzbuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)