import streamlit as st
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# ---------- CUSTOM STYLES ----------
st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
            text-align: center;
            font-family: "Segoe UI", sans-serif;
        }
        .calculator {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 15px;
            width: 340px;
            margin: auto;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        .stTextInput > div > div > input {
            text-align: right;
            background-color: #ffffff;
            color: #000000;
            font-size: 1.5em;
            border-radius: 8px;
            height: 50px;
            border: 2px solid #aaa;
        }
        .stButton > button {
            width: 65px;
            height: 50px;
            margin: 4px;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            border: none;
            color: #ffffff;
            background-color: #0078D4;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #005A9E;
            transform: scale(1.05);
        }
        .orange > button {
            background-color: #E67E22 !important;
        }
        .gray > button {
            background-color: #555 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h2 style='text-align:center;'>🧮 Scientific Calculator</h2>", unsafe_allow_html=True)

# ---------- STATE ----------
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------- FUNCTIONS ----------
def press(value):
    st.session_state.expression += value

def clear():
    st.session_state.expression = ""

def delete():
    st.session_state.expression = st.session_state.expression[:-1]

def evaluate():
    try:
        expr = st.session_state.expression
        expr = expr.replace("^", "**").replace("×", "*").replace("÷", "/")
        expr = expr.replace("π", str(math.pi)).replace("√", "math.sqrt")
        expr = expr.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10").replace("ln", "math.log")
        expr = expr.replace("e", str(math.e))
        result = eval(expr, {"math": math})
        st.session_state.expression = str(round(result, 10))
    except Exception:
        st.session_state.expression = "Error"

# ---------- DISPLAY ----------
st.markdown("<div class='calculator'>", unsafe_allow_html=True)
st.text_input("Display", st.session_state.expression, key="display", disabled=True, label_visibility="collapsed")

# ---------- BUTTONS ----------
buttons = [
    ["7", "8", "9", "÷", "sin"],
    ["4", "5", "6", "×", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "=", "+", "log"],
    ["(", ")", "^", "√", "ln"],
    ["π", "e", "C", "DEL", "AC"]
]

for row in buttons:
    cols = st.columns(5)
    for i, btn in enumerate(row):
        style_class = "orange" if btn in ["=", "+", "-", "×", "÷"] else ""
        with cols[i]:
            if st.button(btn, key=f"{btn}_{i}", use_container_width=True):
                if btn == "=":
                    evaluate()
                elif btn in ["C", "AC"]:
                    clear()
                elif btn == "DEL":
                    delete()
                else:
                    press(btn)

st.markdown("</div>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit — supports sin, cos, tan, log, ln, √, π, e, ^")

