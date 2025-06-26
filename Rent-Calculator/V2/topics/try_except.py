# try:
#   number = int(input("Enter a number: "))
#   print(f"You have entered: {number}")
# except ValueError:
#   print("Please enter valid number!")



# try:
#   number = float(input("Enter a number: "))
#   print(f"You have entered: {number}")
# except ValueError:
#   print("Please enter valid number!")

# try:
#   name = str(input("Enter a string value: "))
#   print(f"You have entered: {type(name)} {name}")
# except ValueError:
#   print("Please enter valid string value!")





# Using multiple except blocks

try:
  num = int(input("Enter number: "))
  value = 10/num
except ValueError:
  print("Invalid Value")
except ZeroDivisionError:
  print("You have entered 0")







# else and finally (Advanced)