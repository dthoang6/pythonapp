# This program reads the contents of the names.txt file one line at a time
def main():
  inputfile = open('names.txt', 'r')

  line1 = inputfile.readline()
  line2 = inputfile.readline()
  line3 = inputfile.readline()

  # Strip the \n from each string
  line1 = line1.rstrip('\n')

  inputfile.close()

  print(line1)
  print(line2)
  print(line3)

main()