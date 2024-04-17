# This program will generate a 7 lottery number from 0 through 9
import random

# Constant number
END = 9           # End of the random number range
START = 0         # Start of the random number range
MAX_DIGITS = 7    # Max number of digits

# Main function
def main():
  # Create a list of 7 items
  numbers = [0] * 7

  # Generate 7 random number using for loop
  for index in range(MAX_DIGITS):
    numbers[index] = random.randint(START, END)

  # Display the lottery number
  print(numbers)

  print('Here are your lottery numbers: ')
  for index in range(MAX_DIGITS):
    print(numbers[index], end = ' ')
  print()

# Call main function
main()