# This program use try/except to display the file

def main():
  filename = input('Enter a filename: ')
  try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
  except IOError:
    print('An error occurred trying to read')
    print('the file', filename)

  # Displaying an exception's default error message
  except ValueError as err:
    # This except clause catches ValueError exceptions, The expressions after the except clause specifies that we are assigning the exception object to the variable err.
    print(err)

  # Have just one except clause to catch all the exceptions that are raised in a try suite, you can specify Exception as the type.
  except Exception as err:
    print(err)
  # The else Clause, the statements in the else suite are executed after the statements in the try suite, only if no exceptions were raised. If the exception is raised, the else suite is skipped.
  else:
      print('Doing whatever you need to do, Dat.')

main()