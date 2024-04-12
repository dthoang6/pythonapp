# This program demonstrate how numbers that are read from a file must be converted from strings  before they are used in a math operation.

def main():
  infile = open('numbers.txt', 'r')
  
  num1 = int(infile.readline())
  num2 = int(infile.readline())
  num3 = int(infile.readline())

  total = num1 + num2 + num3
  print(total)
  infile.close()

main()