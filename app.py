
import streamlit as st
import anthropic

# Initialize the Claude client

api_key = st.secretes["claude_api_key"]
client = anthropic.Anthropic(api_key=api_key)

def get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    # Constructing the prompt for Claude AI
    prompt = f"""
    Based on the following inputs, suggest a personalized meal plan for a diabetic patient:
    - Fasting Sugar Level: {fasting_sugar} mg/dL
    - Pre-meal Sugar Level: {pre_meal_sugar} mg/dL
    - Post-meal Sugar Level: {post_meal_sugar} mg/dL
    - Dietary Preferences: {dietary_preferences}
    
    The meal plan should consider the patient's glucose levels and dietary preferences to provide balanced and healthy meals.
    """

    # API call to Claude AI
    message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class nutritionist. who specializes in diabatic management.",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


    # Returning the generated meal plan
    raw_context = message.content
    itinary = raw_context[0].text
    return itinary

# Streamlit app
st.title("GlucoGuide")
st.write("""
Welcome to GlucoGuide - Your personalized meal planner for managing diabetes.
Enter your sugar levels and dietary preferences to receive customized meal plans that help you maintain healthy glucose levels.
""")

# Sidebar inputs
st.sidebar.header("Input your information")
fasting_sugar = st.sidebar.number_input("Fasting Sugar Level (mg/dL)", min_value=0.0, step=0.1)
pre_meal_sugar = st.sidebar.number_input("Pre-meal Sugar Level (mg/dL)", min_value=0.0, step=0.1)
post_meal_sugar = st.sidebar.number_input("Post-meal Sugar Level (mg/dL)", min_value=0.0, step=0.1)
dietary_preferences = st.sidebar.selectbox(
    "Dietary Preferences",
    ("No preference", "Vegetarian", "Vegan", "Low Carb", "High Protein", "Keto", "Other")
)

# Get meal plan button
if st.sidebar.button("Get Meal Plan"):
    # Call the function to get the meal plan from Claude AI
    meal_plan = get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    
    # Display the meal plan
    st.write("### Your Personalized Meal Plan")
    st.markdown(meal_plan)

