import tkinter as tk
from tkinter import messagebox

def calculate_expense():
    try:
        # Get input values
        persons = int(entry_persons.get())
        rent = float(entry_rent.get())
        grocery = float(entry_grocery.get())
        units = float(entry_units.get())
        unit_price = float(entry_unit_price.get())

        # Calculations
        electricity_bill = units * unit_price
        total = rent + grocery + electricity_bill
        per_person = total / persons

        # Display result
        result_text = (
            f"Electricity Bill: Rs {electricity_bill:.2f}\n"
            f"Total Monthly Expense: Rs {total:.2f}\n"
            f"Per Person Pays: Rs {per_person:.2f}"
        )
        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Rent Calculator")
root.geometry("400x400")
root.config(padx=20, pady=20)

# Input Labels and Entry Fields
tk.Label(root, text="Number of Students:").pack()
entry_persons = tk.Entry(root)
entry_persons.pack()

tk.Label(root, text="Room Rent (Rs):").pack()
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Grocery Cost (Rs):").pack()
entry_grocery = tk.Entry(root)
entry_grocery.pack()

tk.Label(root, text="Electricity Units Used:").pack()
entry_units = tk.Entry(root)
entry_units.pack()

tk.Label(root, text="Price per Unit (Rs):").pack()
entry_unit_price = tk.Entry(root)
entry_unit_price.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_expense).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
result_label.pack()

# Start GUI
root.mainloop()
