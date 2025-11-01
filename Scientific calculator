import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #2C3E50;'>🔢 Scientific Calculator</h1>
    <p style='text-align: center;'>Casio fx-991 style | Built using Streamlit</p>
    """,
    unsafe_allow_html=True
)

# --- Calculator Display ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

display = st.text_input("Display", st.session_state.expression, key="display", disabled=True)

# --- Button Layout ---
buttons = [
    ["7", "8", "9", "/", "sin"],
    ["4", "5", "6", "*", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "=", "+", "log"],
    ["(", ")", "√", "^", "π"],
    ["C", "DEL", "!", "e", "EXP"]
]

# --- Define Calculation Logic ---
def safe_eval(expr):
    try:
        expr = expr.replace("^", "**").replace("√", "math.sqrt(")
        expr = expr.replace("π", str(math.pi)).replace("e", str(math.e))
        expr = expr.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10").replace("EXP", "math.exp")
