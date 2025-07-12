import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.markdown("<h2 style='text-align: center;'>🧮 Calculator by \"Sanwal Mehmood\"</h2>", unsafe_allow_html=True)

# Initialize session state for expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += str(value)

# Function to clear expression
def clear_expression():
    st.session_state.expression = ""

# Create layout: Buttons
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "/", "C"]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if btn == "C":
            if cols[i].button("C"):
                clear_expression()
        else:
            if cols[i].button(btn):
                update_expression(btn)

# Display the expression input box
st.text_input("Expression", st.session_state.expression, key="display")

# Calculate and show result
if st.button("Calculate"):
    try:
        result = eval(st.session_state.expression)
        st.markdown(f"<h3 style='text-align: center; color: white; background-color: #3399ff; padding: 10px; border-radius: 10px;'>Result: {result}</h3>", unsafe_allow_html=True)
    except:
        st.error("Invalid expression!")
