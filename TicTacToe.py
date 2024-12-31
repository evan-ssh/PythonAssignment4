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