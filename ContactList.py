def main():
    contacts = [["Eric idle", "eric@ericidle.com", "+44 20 7946 0958"],
                 ["Guide van Rossum", "mike@murach.com", "559-123-4567"]]
    while True:
     DisplayMenu()
     try:
        command = int(input("Select a command 1 - 5"))
        if command == 1:
         ShowContact(contacts)
        elif command == 2:
         AddContact(contacts)
        elif command == 3:
         RemoveContacts(contacts)
        elif command == 4:
         ViewContact(contacts)
        elif command == 5:
         return False
     except ValueError:
        print("Enter a vaild number")

def DisplayMenu():
   print("COMMAND MENU")
   print("1 - Show Contacts")
   print("2 - Add Contact")   
   print("3 - Remove a contact")
   print("4 - View a contact")
   print("5 - Exit Program")

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

def RemoveContacts(contacts):
 while True:
    try:
        ShowContact(contacts)
        user_input = int(input("Enter number of the contact you'd like to delete"))
        if user_input < 1 or user_input > len(contacts):
            print("Invaild contact")
            continue
        else: 
            contact = contacts.pop(user_input - 1)
            print(f"{contact} was deleted")
            return False
    except ValueError:
       print("Enter a vaild number")

def ViewContact(contacts):
 while True:
    try:
        ShowContact(contacts)
        user_input = int(input("Enter the number of the contact"))
        if user_input < 1 or user_input > len(contacts):
            print("Invaild Contact")
        else:
            contact = contacts[user_input - 1]
            print(f"{contact}")
            return False
    except ValueError:
        print("Enter a vaild number")
main()