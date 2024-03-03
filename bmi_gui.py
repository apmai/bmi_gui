import tkinter as tk
from tkinter import ttk

# Function to calculate and show the BMI
# GUI for BMI Calculator
# Create a BMI calculator using Tkinter


def calculate_and_show_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight_unit.get() == "Pounds (lbs)":
            weight *= 0.453592
        if height_unit.get() == "Inches (in)":
            height *= 0.0254
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 24.9 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and set the message for user's input
message_label = ttk.Label(root, text="Enter your weight and height:")
message_label.pack()

# Weight input
weight_frame = ttk.Frame(root)
weight_frame.pack(padx=10, pady=5)
weight_label = ttk.Label(weight_frame, text="Weight:")
weight_label.pack(side="left")
weight_entry = ttk.Entry(weight_frame, width=10)
weight_entry.pack(side="left")
weight_unit = ttk.Combobox(weight_frame, values=["Kilograms (kg)", "Pounds (lbs)"], state="readonly", width=15)
weight_unit.pack(side="left")
weight_unit.set("Kilograms (kg)")

# Height input
height_frame = ttk.Frame(root)
height_frame.pack(padx=10, pady=5)
height_label = ttk.Label(height_frame, text="Height:")
height_label.pack(side="left")
height_entry = ttk.Entry(height_frame, width=10)
height_entry.pack(side="left")
height_unit = ttk.Combobox(height_frame, values=["Meters (m)", "Inches (in)"], state="readonly", width=15)
height_unit.pack(side="left")
height_unit.set("Meters (m)")

# Button to calculate BMI
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_and_show_bmi)
calculate_button.pack(pady=10)

# Label to display the result
result_label = ttk.Label(root, text="Your BMI will appear here.")
result_label.pack()

# Start the GUI
root.mainloop()
