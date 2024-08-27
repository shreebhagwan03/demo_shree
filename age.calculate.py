import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Function to calculate age
def calculate_age():
    try:
        # Get input from entry fields
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        # Create a birth date object
        birth_date = datetime(year, month, day)
        today = datetime.now()

        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Display the age
        messagebox.showinfo("Your Age", f"You are {age} years old.")
    except ValueError:
        # Error handling for invalid input
        messagebox.showerror("Invalid Input", "Please enter valid numbers for day, month, and year.")


# Creating the main window
window = tk.Tk()
window.title("Age Calculator App")

# Labels and input fields for day, month, and year
tk.Label(window, text="Enter your Birth Date").pack(pady=10)

tk.Label(window, text="Day").pack()
day_entry = tk.Entry(window)
day_entry.pack()

tk.Label(window, text="Month").pack()
month_entry = tk.Entry(window)
month_entry.pack()

tk.Label(window, text="Year").pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Button to calculate age
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=20)

# Running the main loop
window.mainloop()
