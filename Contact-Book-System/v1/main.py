

# step three-----------------------------------------------
contact_list = []
def add_contact():
  name = input("Enter you name: ").strip()
  phone = input("Enter you mobile number: ").strip()
  email = input("Enter you email address: ").strip()

  contacts = {
    "name": name,
    "phone": phone,
    "email": email
  }

  contact_list.append(contacts)
  print(f"========={name} :added successfully! Congrats===========")

# View Contact Method-------------------------------------
def view_contact():
  print("====================List of the Constact===================")
  for contact in contact_list:
    print(f"Name: {contact.get('name')}   ||    Mobile No. {contact.get('phone')}    ||    Email Address: {contact.get('email')}")


# Delete Contact Method-------------------------------------------------
def delete_contact():
  deletable_name = input("Enter name to delete: ").strip()
  for contact in contact_list:
    if contact.get('name').lower() == deletable_name.lower():
      contact_list.remove(contact)
      print(f"Congrats! {deletable_name} is deleted successfully\n")  
      return
  
  print(f"Sorry! {deletable_name} not found")


# step two
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
    break
  else:
    print("Invalid choise, please try again leter!")
