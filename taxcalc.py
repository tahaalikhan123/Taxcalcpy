import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    # Get user input from the GUI
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone_number = phone_entry.get()

    try:
        # Validate and parse numerical inputs
        monthly_salary = float(monthly_salary_entry.get())
        rrsp = float(rrsp_entry.get())
        cpp = float(cpp_entry.get())
        ei = float(ei_entry.get())
        qpp = float(qpp_entry.get())

        # Validate non-negative inputs
        if monthly_salary < 0 or rrsp < 0 or cpp < 0 or ei < 0 or qpp < 0:
            messagebox.showerror("Error", "Inputs cannot be negative.")
            return

        # Calculate taxes and deductions (replace with your calculation logic)
        federal_tax = monthly_salary * 0.15  # Simplified federal tax
        provincial_tax = monthly_salary * 0.10  # Simplified provincial tax
        after_tax_salary = monthly_salary - federal_tax - provincial_tax - rrsp - cpp - ei - qpp

        # Display results in the GUI
        result_label.config(text=f"First Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_number}\n"
                                  f"Monthly Salary Before Taxes: ${monthly_salary:.2f}\n"
                                  f"Federal Tax: ${federal_tax:.2f}\nProvincial Tax: ${provincial_tax:.2f}\n"
                                  f"RRSP: ${rrsp:.2f}\nCPP: ${cpp:.2f}\nEI: ${ei:.2f}\nQPP: ${qpp:.2f}\n"
                                  f"Monthly Salary After Taxes: ${after_tax_salary:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers for salary and deductions.")

# Create the main window
root = tk.Tk()
root.title("Ontario Tax Calculator")

# Create and arrange widgets
first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

monthly_salary_label = tk.Label(root, text="Monthly Salary:")
monthly_salary_label.grid(row=3, column=0)
monthly_salary_entry = tk.Entry(root)
monthly_salary_entry.grid(row=3, column=1)

rrsp_label = tk.Label(root, text="RRSP Deduction:")
rrsp_label.grid(row=4, column=0)
rrsp_entry = tk.Entry(root)
rrsp_entry.grid(row=4, column=1)

cpp_label = tk.Label(root, text="CPP Deduction:")
cpp_label.grid(row=5, column=0)
cpp_entry = tk.Entry(root)
cpp_entry.grid(row=5, column=1)

ei_label = tk.Label(root, text="EI Deduction:")
ei_label.grid(row=6, column=0)
ei_entry = tk.Entry(root)
ei_entry.grid(row=6, column=1)

qpp_label = tk.Label(root, text="QPP Deduction:")
qpp_label.grid(row=7, column=0)
qpp_entry = tk.Entry(root)
qpp_entry.grid(row=7, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.grid(row=8, column=0, columnspan=2)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=9, column=0, columnspan=2)

root.mainloop()