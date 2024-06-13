import tkinter as tk
from tkinter import messagebox

class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced BMI Calculator")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.unit_var = tk.StringVar(value="metric")
        self.unit_label = tk.Label(self, text="Choose units:")
        self.unit_label.pack(pady=5)
        
        self.metric_radio = tk.Radiobutton(self, text="Metric (kg, m)", variable=self.unit_var, value="metric")
        self.metric_radio.pack()
        
        self.imperial_radio = tk.Radiobutton(self, text="Imperial (lbs, inches)", variable=self.unit_var, value="imperial")
        self.imperial_radio.pack()
        
        self.weight_label = tk.Label(self, text="Weight:")
        self.weight_label.pack(pady=5)
        
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()
        
        self.height_label = tk.Label(self, text="Height:")
        self.height_label.pack(pady=5)
        
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()
        
        self.calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack(pady=20)
        
    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            unit = self.unit_var.get()
            
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            
            if unit == "imperial":
                weight *= 0.453592  # lbs to kg
                height *= 0.0254  # inches to meters
                
            bmi = weight / (height ** 2)
            category = self.categorize_bmi(bmi)
            
            result_message = f"Your BMI is: {bmi:.2f}\nThis is considered: {category}"
            messagebox.showinfo("BMI Result", result_message)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()
