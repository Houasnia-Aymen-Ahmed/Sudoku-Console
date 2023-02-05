# import important libraries
import random
from random import shuffle

class Board:

  def __init__(self) -> None:
     # Generates the board when an instance of the class Board is created
     self.grid = self.generate()
    
    # Function that checks for if the grid is full or not, by going through all the board cells
  def checkGrid(self,grid):
      for row in range(0,9):
          for col in range(0,9):
            
            if grid[row][col]==0:
              return False

      return True
    
    
  # Function that iterates through all the cells recursively to make a playable sudoku board.
  def fillGrid(self,grid):
      for i in range(0,81):
        row=i//9
        col=i%9
        
        if grid[row][col]==0:
          # The first 3 variables for the rows, cols and 3x3 square
          row_set = set(grid[row])
          col_set = set([grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]])
          subgrid_set = set(number for sublist in grid[row//3*3:row//3*3+3] for number in sublist[col//3*3:col//3*3+3])
          
          # To make the generator eve, more efficient and optimized, this variable is used to store 
          # only the values that haven't been used in the board ( following the rules of sudoku )
          valid_values = set(range(1, 10)) - (row_set | col_set | subgrid_set)
          valid_values = list(valid_values)
          
          # Shuffle the values to make sure we get a diffrent values, either way we would always
          # Start filling the board from 1 to 9, and we would get always the same board
          shuffle(valid_values)
          
          # Fill the board making sure that the value isn't duplicated
          for value in valid_values:
              grid[row][col]=value
              
              # Make sure the generator stops when the board is full
              if self.checkGrid(grid):
                  return True
              else:
                  if self.fillGrid(grid):
                    return True
          break
      grid[row][col]=0
      
  def generate(self):
    grid =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    self.fillGrid(grid)
    return grid

  # Remove some values from the board to make it playable ( either way we would have a solved board ).
  # The number of values is removed based on the level the user wants to play. if he don't choose or something went wrong, level 2 is chosen automatically
  def Level(self,board=None,mode = '2'):

    if board is None:
      board = self.grid

    tempBoard = board.copy()

    if mode == '3' : mode = random.randint((81-23),(81-17))
    elif mode == '2' : mode = random.randint((81-33),(81-27))
    elif mode == '1' : mode = random.randint((81-43),(81-37))
    else:
      print('You Entered a wrong mode, medium will be chosen automatically')
      mode = random.randint((81-33),(81-27))

    fullValues = list(range(0,81))
    removed = random.sample(fullValues, mode)

    for value in removed:
      row = value//9
      col = value%9
      tempBoard[row][col] = 0
    return tempBoard

  # Display the board in a way that is so close to the actual sudoky board
  def displayBoard(self,board=None):
    if board is None:
      board = self.grid

    for i in range(len(board)):
      if  i%3 == 0:
          print('','-'*39)
      for j in range(len(board)):
        if j == len(board)-1:
          if board[i][j] == 0:
            print('',' ',end='')
          else:
            print('',board[i][j],end='')
          if  (i+1)/3 == 0 or (i+1)/3 == 1 or (i+1)/3 == 2 or (i+1)/3 == 3:
            print(' ||')
          else:
            print(' ||\n')
        else:
          if j == 0:
            print('|',end='')
          if  j%3 == 0:
            print('|',end='')

          if board[i][j] == 0:
            print('',' ',end=' |')
          else:
            print('',board[i][j],end=' |')
      if i == len(board)-1:
        print('','-'*39)

