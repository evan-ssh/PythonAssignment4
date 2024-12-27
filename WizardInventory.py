import random
def main():
 playerinventory = ["Wooden staff", "Wizard Hat", "Cloth"]
 while True:
    DisplayMenu()
    try:
        command =int(input("Enter a command"))
        if command > 4:
            print("Enter a vaild command")
            continue
        if command == 1:
            ShowItems(playerinventory)
        elif command == 2:
            GrabItems(playerinventory)
        elif command == 3:
            DropItem(playerinventory)
        elif command == 4:
            print("GoodBye")
            return False
    except ValueError:
        print("Enter a vaild number")

def DisplayMenu():
    print("COMMAND MENU")
    print("1 - Show all items")
    print("2 - Grab an item")
    print("3 - Drop an item")
    print("4 - Exit the program")

def ShowItems(player_inventory):
   for i, items in enumerate(player_inventory):
      print(i+1,items)

def GrabItems(player_inventory):
 find_items = ["Potion of Invisibility", "Cool hat", "Raggedy boots", "Shabby sword"]
 ShowItems(player_inventory)
 for items in find_items:
    if len(player_inventory) > 3:
        print("You can only hold 4 items - drop one first.")
        break
    else:
        player_inventory.append(random.choice(find_items))
        break

def DropItem(player_inventory):
 while True:
  try:  
    user_number = int(input("Number for item to delete: "))
    if user_number < 1 or user_number > len(player_inventory):
       print("Invaild number for item in inventory")
       continue
    else:
        item = player_inventory.pop(user_number-1)
        print(f"{item} was dropped from the inventory.")
        break
  except ValueError:
     print("enter a vaild number in inventory")
main()