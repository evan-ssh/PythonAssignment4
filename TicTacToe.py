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
    print(row)
    if row.count(row[0] == len(row) and row[0]) != 0:
      print("Winner!")

  #diagonal cases
  diags = []
  for col, row in enumerate(reversed(range(len(board)))):
    diags.append(board[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
       print("winner")

  diags = []
  for i in range(len(board)):
    diags.append(board[i][i])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
      print("winner")

  #vert winner
  for col in range(len(board)):
    verts  = []
    for row in board:
      verts.append(row[col])
    if verts.count(verts[0]) == len(verts) and verts[0] != 0:
      print("Winner")