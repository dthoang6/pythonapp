# This program displays a random number in the range of 1 through 10
import random

def main():
  # random module, randint, randrange, uniform Functions
  # Assign a random number in the range of 0 through 9 to the number variable
  number = random.randint(1, 10)
  print('The random integer number in the range 1 - 10 is: ', number)

  # Specify both a starting value and ending limit for the sequence
  number = random.randrange(6, 10)
  print('The random integer number in the range 6 - 10 is: ', number)

  # Specify starting value, ending limit, and step value
  number = random.randrange(5, 100, 20)
  print('The random integer number in the range 5 - 100 with stepping value = 20 is: ', number)

  # Both the randint and randrange functions return an integer number
  # The random() function returns a random floating point number in the range of 0.0 up to 1.0
  number = random.random()
  print("The random float number in the range of 0.0 up to 1.0: ", number)

  number = random.random() * 10
  print("The random float number in the range of 1.0 up to 10.0: ", number)

  # The uniform function return a random floating point number, but allows you to specify the range of values to select from
  number = random.uniform(5.0, 15.0)
  print('The random float number in the range of 5.0 to 15.0: ', number)


main()