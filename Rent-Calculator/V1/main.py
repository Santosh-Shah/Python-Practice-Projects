# Rent Calculator System

person = int(input("Enter numbers of Student lived here: "))
room_rent_cost = int(input("Enter monthly rent of room: "))
grocery_cost = int(input("Enter monthly Grocery Cost: "))
elect_unit = int(input("Enter total unit of electricity of month: "))
per_unit_cost= int(input("Enter price of per unit: "))

total_elect_bills = elect_unit * per_unit_cost
total_monthly_exp = total_elect_bills + (room_rent_cost + grocery_cost)
per_person_exp = total_monthly_exp / person

print("-----------------------------------------------------------")
print(f"Your Total Electricity Bills to pay: {total_elect_bills}")
print(f"Your monthly expenses: {total_monthly_exp}")
print(f"Per Person have to pay: {per_person_exp}")
