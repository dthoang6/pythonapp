# This program reads and display the contents of the names.txt file
def main():
  infile = open('names.txt', 'r') # Open the file
  file_contents = infile.read()   # Read the file's contents
  infile.close()                  # Close the file

  print(file_contents)            # Print the data that was read into memory

main()