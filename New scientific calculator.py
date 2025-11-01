import streamlit as st
import math

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.markdown(
    """
    <h1 style="text-align:center;">🔢 Scientific Calculator (Casio fx-991 Style)</h1>
    <p style="text-align:center; color:gray;">Built with Streamlit | Supports basic & scientific operations</p>
    """,
    unsafe_allow_html=True
)

# ---------- SESSION STATE ----------
if "input" not in st.session_state:
    st.session_state.input = ""

# ---------- FUNCTIONS ----------
def append(symbol):
    st.session_state.input += symbol

def clear():
    st.session_state.input = ""

def delete():
    st.session_state.input = st.session_state.input[:-1]

def evaluate():
    try:
        expr = st.session_state.input
        expr = expr.replace("^", "**")
        expr = expr.replace("×", "*").replace("÷", "/")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")
        expr = expr.replace("e", str(math.e))
        result = eval(expr, {"math": math})
        st.session_state.input = str(result)
    except:
        st.session_state.input = "Error"

# ---------- DISPLAY ----------
st.text_input("Display", value=st.session_state.input, key="display", disabled=True)

# ---------- BUTTON LAYOUT ----------
buttons = [
    ["7", "8", "9", "÷", "sin"],
    ["4", "5", "6", "×", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "=", "+", "log"],
    ["(", ")", "^", "√", "ln"],
    ["π", "e", "C", "DEL", "AC"]
]

# ---------- BUTTON GRID ----------
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == "=":
                evaluate()
            elif btn == "C":
                clear()
            elif btn == "DEL":
                delete()
            elif btn == "AC":
                clear()
            else:
                append(btn)

st.caption("Made with ❤️ using Streamlit | Supports sin, cos, tan, log, ln, √, π, e, ^")

