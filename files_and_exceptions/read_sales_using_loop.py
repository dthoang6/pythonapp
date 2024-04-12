# This program will using while loop or for loop to read the file

def main():
  print('Using while loop to read file: ')
  sale_file = open('sales.txt', 'r')  # Open the file
  line = sale_file.readline()         # Read first line of file

  while line != '':                   # Value return from readline is not a string
    print(line.rstrip('\n'))          # It is still a string, need to convert for math
    line = sale_file.readline()       # Read next line

  sale_file.close()

  print('Using for loop to read file: ')
  read_file_for_loop()


# Function read_file_for_loop using for loop to read lines
def read_file_for_loop():
  sale_file = open('sales.txt', 'r')  # Open the file
  for line in sale_file:
    print(line.rstrip('\n'))          # It is still a string, need to convert for math
  sale_file.close()

main()