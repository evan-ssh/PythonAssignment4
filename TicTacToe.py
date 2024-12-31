def main():
 game = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]
 WinCases(game)
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