# This program allows the user to choose various geometry calculations from a menu. This program imports the circle and rectangle modules.

import circle
import rectangle

# Constants for menu choice
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_CHOICE = 4
QUIT_CHOICE = 5

def main():
  # The choice variable controls the loop and holds the user's menu choice
  choice = 0

  while choice != QUIT_CHOICE:
    display_menu()

    choice = int(input('Enter your choice: '))

    # Perform selected action
    if choice == AREA_CIRCLE_CHOICE:
      radius = float(input("Enter the circle's radius: "))
      print('The area of circle is: ', circle.area(radius))
    elif choice == CIRCUMFERENCE_CHOICE:
      radius = float(input("Enter the radius's circle: "))
      print('The circumference of a circle is: ', circle.circumference(radius))
    elif choice == AREA_RECTANGLE_CHOICE:
      width = float(input("Enter the width's rectangle: "))
      length = float(input("Enter the length's rectangle: "))
      print('The area of a rectangle is: ', rectangle.area(width, length))
    elif choice == PERIMETER_CHOICE:
      width = float(input("Enter the width's rectangle: "))
      length = float(input("Enter the length's rectangle: "))
      print('The perimeter of a rectangle is: ', rectangle.perimeter(width, length))
    elif choice == QUIT_CHOICE:
      print('Exiting the program...')
    else:
      print('Error: invalid selection.')

# The display_menu function displays a menu
def display_menu():
  print('     MENU')
  print('1) Area of a circle')
  print('2) Circumference of a circle')
  print('3) Area of a rectangle')
  print('4) Perimeter of a rectangle')
  print('5) Quit')

# Call main function
main()