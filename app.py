import gradio as gr
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define prediction function
def predict_churn(gender, num_products, is_active_member, estimated_salary, complain, point_earned, age_group):
    # Convert categorical inputs
    gender = 1.0 if gender == "Male" else 0.0
    is_active_member = 1 if is_active_member == "Yes" else 0
    complain = 1 if complain == "Yes" else 0
    age_group = {"Middle Age": 0, "Young": 1, "Senior": 2}[age_group]

    # Prepare input data
    input_data = np.array([[gender, num_products, is_active_member, estimated_salary, complain, point_earned, age_group]])
    
    # Predict churn
    prediction = model.predict(input_data)
    
    return "🎉 Retained Customer!" if prediction[0] == 0 else "😢 Churned Customer!"

# Create Gradio interface
iface = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Radio(["Female", "Male"], label="Gender"),
        gr.Dropdown([1, 2, 3], label="Number of Products Bought"),
        gr.Radio(["No", "Yes"], label="Active Member?"),
        gr.Slider(0, 1000000, step=1000, label="Estimated Salary"),
        gr.Radio(["No", "Yes"], label="Complain Registered?"),
        gr.Slider(100, 1000, step=50, label="Points Earned"),
        gr.Radio(["Middle Age", "Young", "Senior"], label="Which Age Group"),
    ],
    outputs="text",
    title="🔮 Bank Churn Prediction App",
    description="Enter customer details to predict churn risk!"
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch(share=True)
