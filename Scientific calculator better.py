import streamlit as st
import math

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# Custom CSS styling for Casio look
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
        color: white;
        text-align: center;
    }
    .calculator {
        background-color: #2C2C2C;
        padding: 20px;
        border-radius: 15px;
        width: 320px;
        margin: auto;
        box-shadow: 0 0 15px #000;
    }
    .stTextInput > div > div > input {
        text-align: right;
        background-color: #111;
        color: #0FF;
        font-size: 1.4em;
        border-radius: 8px;
        height: 50px;
        border: 2px solid #444;
    }
    .stButton > button {
        width: 60px;
        height: 45px;
        margin: 4px;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: 600;
        color: white;
        background-color: #3A3A3A;
        border: none;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background-color: #0078D4;
        color: white;
        transform: scale(1.05);
    }
    .stButton > button:active {
        background-color: #005A9E;
    }
    .orange > button {
        background-color: #E67E22 !important;
    }
    .blue > button {
        background-color: #2980B9 !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#00FFFF;'>Casio-Style Scientific Calculator</h2>", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------
if "expression" not in st.session_state:
    st.session_state.expression = ""

# -------------------- FUNCTIONS --------------------
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
        st.session_state.expression = str(result)
    except Exception:
        st.session_state.expression = "Error"

# -------------------- DISPLAY --------------------
st.markdown("<div class='calculator'>", unsafe_allow_html=True)
st.text_input("Display", st.session_state.expression, key="display", disabled=True)

# -------------------- BUTTON GRID --------------------
buttons = [
    ["7", "8", "9", "÷", "sin"],
    ["4", "5", "6", "×", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "=", "+", "log"],
    ["(", ")", "^", "√", "ln"],
    ["π", "e", "C", "DEL", "AC"]
]

for row in buttons:
    cols = st.columns(5, gap="small")
    for i, btn in enumerate(row):
        # Special color buttons
        if btn in ["=", "+", "-", "×", "÷"]:
            style_class = "orange"
        elif btn in ["sin", "cos", "tan", "log", "ln", "√"]:
            style_class = "blue"
        else:
            style_class = ""
        with cols[i]:
            if st.container():
                btn_clicked = st.button(btn, key=btn + str(row))
                if btn_clicked:
                    if btn == "=":
                        evaluate()
                    elif btn == "C" or btn == "AC":
                        clear()
                    elif btn == "DEL":
                        delete()
                    else:
                        press(btn)

st.markdown("</div>", unsafe_allow_html=True)

st.caption("Made with ❤️ using Streamlit | Supports sin, cos, tan, log, ln, √, π, e, ^")

