def get_user_input():
    """Get user input for weight, height, and unit preference."""
    while True:
        try:
            unit = input("Choose units: (1) Metric (kg, m) or (2) Imperial (lbs, inches): ")
            if unit not in ('1', '2'):
                print("Invalid choice. Please select 1 or 2.")
                continue
            
            if unit == '1':
                weight = float(input("Enter your weight in kilograms (kg): "))
                height = float(input("Enter your height in meters (m): "))
            else:
                weight = float(input("Enter your weight in pounds (lbs): "))
                height = float(input("Enter your height in inches (in): "))

            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers. Please try again.")
                continue

            return weight, height, unit
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")

def calculate_bmi(weight, height, unit):
    """Calculate BMI using the provided weight, height, and unit system."""
    if unit == '2':  # Convert from imperial to metric
        weight = weight * 0.453592  # lbs to kg
        height = height * 0.0254  # inches to meters
    
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """Categorize the BMI into different ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to execute the BMI calculator."""
    print("Welcome to the Advanced BMI Calculator!")
    
    weight, height, unit = get_user_input()
    bmi = calculate_bmi(weight, height, unit)
    category = categorize_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"This is considered: {category}")

    # Additional suggestions based on BMI category
    if category == "Underweight":
        print("Suggestion: It's important to eat a nutritious diet and possibly consult with a healthcare provider.")
    elif category == "Normal weight":
        print("Suggestion: Keep maintaining a balanced diet and regular physical activity.")
    elif category == "Overweight":
        print("Suggestion: Consider a balanced diet and regular exercise to reach a healthier weight.")
    elif category == "Obesity":
        print("Suggestion: It's advisable to consult with a healthcare provider for personalized advice.")

if __name__ == "__main__":
    main()

