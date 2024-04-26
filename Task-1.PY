import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 24.9 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        messagebox.showinfo("BMI Calculator", f"Your BMI is: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")

height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
