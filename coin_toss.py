""" 
  Repeat 10 times:
    If a random number in the range of 1 through 2 equals 1 then:
      Display 'Heads'
    else:
      Display 'Tails

"""
import random

def main():
  for _ in range(10):
    toss = random.randint(1,2)
    if toss == 1:
      print('Head')
    else:
      print('Tails')

main()
#####
# Constants
HEADS = 1
TAILS = 2
TOSSES = 10
def coin_game():
  for _ in range(TOSSES):
    # Simulate the coin toss.
    if random.randint(HEADS, TAILS) == HEADS:
      print('Heads')
    else:
      print('tails')
coin_game()