# This program writes three lines of data to a file

def main():
  outfile = open('names.txt', 'w')    # Open the file name
  outfile.write('Tom Hoang\n')        # Write the name to a file
  outfile.write('Dat Hoang\n')
  outfile.write('Software Engineer\n')

  # Get name from users
  name = input('Enter your name: ')
  outfile.write(name + '\n')          # Add new line

  outfile.close()    # Close the file, close the connection from program to file

  # Append data to file
  outfile = open('names.txt', 'a')

  # Can write String to file, Have to convert other data type to String
  number = int(input('Enter your special numbers: '))   # Get integer number

  outfile.write(str(number))                            # Convert to string and write to file


main()