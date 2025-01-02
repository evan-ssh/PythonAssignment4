def main():
 game = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]
 players = ["1","2"]
 round = 1

 while True:
  round += 1
  if round % 2:
    print(players[1], "turn")
    row = int(input("Enter a row"))
    col = int(input("Enter a col"))
  else:
    print(players[0], "turn")
    row = int(input("Enter a row"))
    col = int(input("Enter a col"))
    

 
 


def WinCases(game):
    
  # horizontal cases

  for row in game:
    print(row)
    if row.count(row[0] == len(row) and row[0]) != 0:
      print("Winner!")

  #diagonal cases
  diags = []
  for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
       print("winner")

  diags = []
  for i in range(len(game)):
    diags.append(game[i][i])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
      print("winner")

  #vert winner
  for col in range(len(game)):
    verts  = []
    for row in game:
      verts.append(row[col])
    if verts.count(verts[0]) == len(verts) and verts[0] != 0:
      print("Winner")