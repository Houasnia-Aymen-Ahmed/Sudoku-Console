import random
from random import shuffle

class Board:

  def __init__(self) -> None:
     self.grid = self.generate()
  def checkGrid(self,grid):
      for row in range(0,9):
          for col in range(0,9):
            if grid[row][col]==0:
              return False
      return True
      
  def fillGrid(self,grid):
      for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
          row_set = set(grid[row])
          col_set = set([grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]])
          subgrid_set = set(number for sublist in grid[row//3*3:row//3*3+3] for number in sublist[col//3*3:col//3*3+3])
          valid_values = set(range(1, 10)) - (row_set | col_set | subgrid_set)
          valid_values = list(valid_values)
          shuffle(valid_values)
          for value in valid_values:
              grid[row][col]=value
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

