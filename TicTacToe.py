def main():
 board = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]
 players = ["X","O"]
 round = 1

 while True:
  round += 1
  ShowBoard(board)
  if round % 2:
    print(players[1], "turn")
    PlayerTwoTurn(board,players)
  else:
    print(players[0], "turn")
    PlayerOneTurn(board,players)

#player one
def PlayerOneTurn(board,players):
 while True:
  try:
   row = int(input("Select a row")) - 1
   col = int(input("Select a col")) - 1
   if board[row][col] != 0:
    print("Spot has been taken pick another")
    continue
   else:
    board[row][col] = players[0]
    break
  except ValueError:
    print("Enter an integer")
  except IndexError:
   print("Did u enter a number within the range (1-3)?")
  except Exception as e:
   print(f"Something went wrong", {e})


#player two
def PlayerTwoTurn(board,players):
 while True:
  try:
    row = int(input("Select a row: ")) - 1
    col = int(input("Select a col: "))
    if board[row][col] != 0:
     print("Spot has been taken pick another")
     continue
    else:
     board[row][col] = players[1]
     break
  except ValueError:
    print("Enter an integer")
  except IndexError:
    print("Did u enter a number within the range (1-3)?")
  except Exception as e:
    print("Something went wrong", {e})

def ShowBoard(board):
 for i, rows in enumerate(board):
  print(i+1, rows)


def WinCases(board):
    
  # horizontal cases

  for row in board:
   if row[0] == row[1] == row[2] and row[0] != 0:
    print(f"{row[0]} is the winner")
  

  #diagonal cases
  for _ in board:
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
      print(f"{board[[2][0]]}")
  for _ in board:#top left to bottom right
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
      print(f"{board[0][0]} is the winner")

  #vert winner
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
      print(f"{board[0][col]} is the winner")
      
    