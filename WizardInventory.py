import random
def main():
 playerinventory = ["Wooden staff", "Wizard Hat", "Cloth"]
 while True:
    command = input("Enter a command")
    if command == "show":
        ShowItems(playerinventory)
    elif command == "grab":
        GrabItems(playerinventory)
def DisplayMenu():
    print("COMMAND MENU")
    print("Show - Show all items")
    print("Grab - Grab an item")
    print("Edit - Edit an item")
    print("Exit - Exit the program")

def ShowItems(player_inventory):
   for i, items in enumerate(player_inventory):
      print(i+1,items)

def GrabItems(player_inventory):
 find_items = ["Potion of Invisibility", "Cool hat", "Raggedy boots", "Shabby sword"]
 ShowItems(player_inventory)
 for items in find_items:
    if len(player_inventory) > 4:
        print("You can only hold 4 items - drop one first.")
    else:
        player_inventory.append(random.choice(find_items))
        break
main()