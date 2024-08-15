import tkinter as tk
import time

# Function to update the time
def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update the time every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('Arial', 40), background='black', foreground='white')
label.pack(anchor='center')

# Call the update_time function to start the clock
update_time()

# Run the clock
root.mainloop()
