"""
This is a fun sudoku game without a GUI, it's not optimized or something, i just made it for fun, and maybe people will give me some advice to make it better
Have fun playing it or browsing it's code. if you have any questions you can ask me anytime, and i'll try to respond as fast as i can.
See ya
"""

from Functions import *
from BoardGenerator import Board

displayWelcome()
choice = input('Mode: ')

global sudoku_board
board = Board()
sudoku_board = board.grid
sudoku_board = board.Level(None,choice)

# Function that displays the board in a readable way, as close as possible to the actual game

def fillPosition(position,value) -> None:
  listOfGlobals = globals()
  listOfGlobals['sudoku_board'][position[0]-1][position[1]-1] = value

def Game():

  value = position = None

  while True:
    board.displayBoard(sudoku_board)

    try:
      row, col = [x for x in input("Enter the position (from 1 to 9 for both rows & columns): ").split()]
      
      if row.lower() =='break' or row.lower() =='q' or row.lower() =='quit':
        print('Board still undone, You lost')
        break

      position = (int(row),int(col))

      if checkValidPosition(position) == False:
        print('Please enter a valid position')
        continue

      value = int(input('Enter the Value for this position: '))

      if checkValue(value) == False:
        print('Please enter a valid value')
        continue
    
      fillPosition(position,value)

      if checkPosition(sudoku_board,position,value) == True:
        checkSquare(getSquare(sudoku_board,findSquare(position)),value,True)

      if checkBoard(sudoku_board) == True:
        break
    except:
      print('Enter a valid value')
      continue
"""
board.displayBoard(sudoku_board)

row, col = [x for x in input("Enter the position (from 1 to 9 for both rows & columns): ").split()]
value = int(input('Enter the Value for this position: '))
checkColumn(sudoku_board,int(col)-1,value)


"""
check = Game()

if check == True:
  board.displayBoard(sudoku_board)
  print('You Won')
