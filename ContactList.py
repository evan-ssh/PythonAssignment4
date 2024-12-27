def main():
    contacts = [["Eric idle", "eric@ericidle.com", "+44 20 7946 0958"],
                 ["Guide van Rossum", "mike@murach.com", "559-123-4567"]]
    while True:
     DisplayMenu()
     try:
        command = int(input("Select a command 1 - 4"))
        if command == 1:
         ShowContact(contacts)
        elif command == 2:
           AddContact(contacts)
     except ValueError:
        print("Enter a vaild number")

def DisplayMenu():
   print("COMMAND MENU")
   print("1 - Show Contacts")
   print("2 - Add Contact")   

def ShowContact(contacts):
    for i, contact in enumerate(contacts):
        print(i+1, contact[0])

def AddContact(contacts):
 name = input("Enter a name: ")
 email = input("Enter an email: ")
 phone = input("Enter a phone number: ")
 new_contact = [name, email, phone]
 contacts.append(new_contact)
 print("Contact was added")


main()