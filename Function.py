# This file contains some usefull function for the game
import numpy as np

def displayWelcome() -> None:
    print('','='*30+" WELCOME! "+'='*30,)
    print('|                                                                      |')
    print('|                             SUDOKU Game                              |')
    print('|                                                                      |')
    print('|                           Choose your mode                           |')
    print('|                                                                      |')
    print('|                        for EASY MODE choose 1                        |')
    print('|                                                                      |')
    print('|                       for MEDIUM MODE choose 2                       |')
    print('|                                                                      |')
    print('|                        for HARD MODE choose 3                        |')
    print('|                                                                      |')
    print('|                (: (: (: Have fun playing it :) :) :)                 |')
    print('|                                                                      |')
    print('','='*70)

# Checks the validity of value ( must be between 1-9)
def checkValue(value):
  check = True
  if value < 1 or value > 9:
    check = False
  return check

# Function to check wether the user have entered a valid position of the board
def checkValidPosition(position):
  check = True
  if position[0] < 1 or position[0] > 9 or position[1] < 1 or position[1] > 9:
    check = False
  return check

# Function that checks if a row is correctly complete
def checkRow(board,row_position,value,disp=False):
    
  check = True
  countValueInRow = board[row_position-1].tolist().count(value)
    
  if countValueInRow > 1:
    check = False
  return (check,countValueInRow)

# Function that checks if a col is correctly complete
def checkColumn(board,column_position,value,disp=False):
    
  check = True
  column = [row[column_position-1] for row in board]
  countValueInCol = column.count(value)

  if countValueInCol > 1:
    check = False
  return (check,countValueInCol)

# Checks if the value is duplicated in a row or a col
def checkPosition(board,position,value):
  check = True

  if (checkColumn(board,position[1],value)[0] == False):
    print("Be carfull, This item is already in this column")
    check = False
    
  elif (checkRow(board,position[0],value)[0] == False):
    print("Be carfull, This item is already in this row")
    check = False
    
  else:
    check = True
  return check

# Check if the value is duplicated in the 3x3 square
def checkSquare(miniboard,value,disp=False):
  check = True
  count = np.count_nonzero(miniboard == value)
  
  if count > 1:
    check = False
    if disp == True:
      print("Be carfull, This item is already in this Square")
  return check

# Find the square of a given position
def findSquare(position):
  row = position[0]
  col = position[1]
  square = 0

  if row in [0,1,2]:
        
    if col in [0,1,2]:
      square = 1
    elif col in [3,4,5]:
      square = 2
    elif col in [6,7,8]:
      square = 3
    else:
      print("Error row (1-3)")

  elif row in [3,4,5]:
    
    if col in [0,1,2]:
      square = 4
    elif col in [3,4,5]:
      square = 5
    elif col in [6,7,8]:
      square = 6
    else:
      print("Error row (4-6)")

  elif row in [6,7,8]:
    
    if col in [0,1,2]:
      square = 7
    elif col in [3,4,5]:
      square = 8
    elif col in [6,7,8]:
      square = 9
    else:
        print("Error row (7-9)")
  else:
    print("Error")

  return square

# Get the 3x3 square by it's position
def getSquare(board,square):
    
  miniboard = None
  if square == 1:
    miniboard = board[0:3,0:3]
  elif square == 2:
    miniboard = board[0:3,3:6]
  elif square == 3:
    miniboard = board[0:3,6:9]
  elif square == 4:
    miniboard = board[3:6,0:3]
  elif square == 5:
    miniboard = board[3:6,3:6]
  elif square == 6:
    miniboard = board[3:6,6:9]
  elif square == 7:
    miniboard = board[6:9,0:3]
  elif square == 8:
    miniboard = board[6:9,3:6]
  elif square == 9:
    miniboard = board[6:9,6:9]
  else:
    print('ERROR!!')
  return miniboard

# Gives the number of cells that are still non-filled
def checkBoard(board):
  check = True
  fcheck, counter = checkFull(board)
    
  if  fcheck == False:
    check = False
    print('There is still %d unfilled positions on the board'%counter)
    return check

  for i in range(1,10):
    for j in range(1,10):
        
      ccheck, _ = checkColumn(board,i,j)
      rcheck, _ = checkRow(board,i,j)
      scheck = checkSquare(getSquare(board,i),j)
    
      if ccheck == False or rcheck == False or scheck == False:
        check = False
        break
        
    if check == False:
      break
  
  return check

# Checks wether the function is full or not ( other way to check is in the boardGenerator.py file )
def checkFull(board):
  check = True
  counter = 0
  for i in range(9):
    for j in range(9):
      x = str(board[i][j])
      if x not in ['1','2','3','4','5','6','7','8','9']:
        check = False
        counter+=1
        
  return (check,counter)
