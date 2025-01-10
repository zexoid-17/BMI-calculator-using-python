import gradio as gr

def calculate_bmi(weight, height, height_unit, age, gender):
    try:
        # Convert height to meters if input is in inches
        if height_unit == "Inches":
            height = height * 0.0254
        
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            status = "Underweight"
            advice = "You should eat more nutritious food and consult a dietitian."
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
            advice = "Keep maintaining a balanced diet and regular exercise."
        elif 25 <= bmi < 29.9:
            status = "Overweight"
            advice = "Consider adopting a healthy eating plan and increasing physical activity."
        else:
            status = "Obesity"
            advice = "Consult a healthcare provider for a tailored weight management plan."
        
        if gender.lower() == "male":
            ideal_weight = 50 + 0.9 * ((height * 100) - 152)
        else:
            ideal_weight = 45.5 + 0.9 * ((height * 100) - 152)
        ideal_weight = round(ideal_weight, 2)
        
        return {
            "BMI": bmi,
            "Status": status,
            "Advice": advice,
            "Ideal Weight": f"{ideal_weight} kg"
        }
    except Exception as e:
        return {"Error": str(e)}

def gradio_interface(weight, height, height_unit, age, gender):
    result = calculate_bmi(weight, height, height_unit, age, gender)
    output = (
        f"**BMI**: {result.get('BMI')}\n"
        f"**Status**: {result.get('Status')}\n"
        f"**Advice**: {result.get('Advice')}\n"
        f"**Ideal Weight**: {result.get('Ideal Weight')}\n"
    )
    return output

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Number(label="Weight (kg)", value=70),
        gr.Number(label="Height", value=1.75),
        gr.Radio(choices=["Meters", "Inches"], label="Height Unit", value="Meters"),
        gr.Number(label="Age (years)", value=25),
        gr.Radio(choices=["Male", "Female"], label="Gender", value="Male")
    ],
    outputs="markdown",
    title="Advanced BMI Calculator",
    description="Calculate your BMI with options for height in meters or inches, health recommendations, and ideal weight suggestions.",
    theme="compact"
)

if __name__ == "__main__":
    iface.launch()
