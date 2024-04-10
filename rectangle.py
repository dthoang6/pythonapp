# The rectangle module has functions that perform calculations related to rectangles

# Notice that both the circle.py and rectangle.py do not contain code that calls the function. It will be done by the program or programs that import these modules.

# The area function accepts a rectangle's width and length as arguments and returns the rectangle's area
def area(width, length):
  return width * length

# The perimeter function accept a rectangle's width and length as arguments and returns the rectangle's perimeter
def perimeter(width, length):
  return 2 * (width + length)