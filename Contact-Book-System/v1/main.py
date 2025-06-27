


def show_menu():
  print("=============Contact Book Menu===============")
  print("1 - Add Contact")
  print("2 - View Contact")
  print("3 - Delete Contact")
  print("4 - Exit")
  print("=============================================")


# step one - starting point
while True:
  show_menu()
  chosenNum = int(input("Enter you option from 1 - 4: "))
  if chosenNum == 1:
    add_contact()
  elif chosenNum == 2:
    view_contact()
  elif chosenNum == 3:
    delete_contact()
  elif chosenNum == 4:
    print("Exiting Book, GoodBye!")
  else:
    print("Invalid choise, please try again leter!")
