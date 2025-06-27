
# Rent Calculator System
def calculate_rent():
  try:
    person = int(input("Enter numbers of Student lived here: "))
    room_rent_cost = float(input("Enter monthly rent of room: "))
    grocery_cost = float(input("Enter monthly Grocery Cost: "))
    elect_unit = float(input("Enter total unit of electricity of month: "))
    per_unit_cost= float(input("Enter price of per unit: "))

    total_elect_bills = elect_unit * per_unit_cost
    total_monthly_exp = total_elect_bills + (room_rent_cost + grocery_cost)
    per_person_exp = total_monthly_exp / person

    print("\n---------------- Rent Calculator Summary ----------------")
    print(f"Your Total Electricity Bills to pay: {total_elect_bills: .2f}")
    print(f"Your monthly expenses: {total_monthly_exp: .2f}")
    print(f"Per Person have to pay: {per_person_exp: .2f}")
  except ValueError:
    print("❌ Please enter valid numeric values only.")



if __name__ == "__main__":
  calculate_rent()
