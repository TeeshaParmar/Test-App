import streamlit as st
import math
import numpy as np

# Page configuration
st.set_page_config(page_title="Casio fx-991 Calculator", layout="centered")

# Custom CSS for Casio-like styling
st.markdown("""
<style>
    .main {
        background-color: #2c3e50;
        padding: 20px;
    }
    .stButton > button {
        width: 100%;
        height: 50px;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid #34495e;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.3rem;
    }
    .calculator-display {
        background: linear-gradient(145deg, #8b9f7f, #a8c69f);
        padding: 20px;
        border-radius: 10px;
        border: 3px solid #5a6d54;
        margin-bottom: 20px;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
    }
    .display-text {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        color: #1a1a1a;
        text-align: right;
        min-height: 60px;
        word-wrap: break-word;
    }
    .calculator-body {
        background: linear-gradient(145deg, #34495e, #2c3e50);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }
    h1 {
        color: #ecf0f1;
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'current_value' not in st.session_state:
    st.session_state.current_value = ''
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'previous_value' not in st.session_state:
    st.session_state.previous_value = ''
if 'new_number' not in st.session_state:
    st.session_state.new_number = True
if 'memory' not in st.session_state:
    st.session_state.memory = 0
if 'angle_mode' not in st.session_state:
    st.session_state.angle_mode = 'DEG'  # DEG or RAD

def safe_eval(value):
    """Safely evaluate mathematical expression"""
    try:
        return float(value)
    except:
        return 0

def update_display(value):
    """Update calculator display"""
    st.session_state.display = str(value)

def append_to_display(char):
    """Append character to display"""
    if st.session_state.new_number:
        st.session_state.display = char
        st.session_state.new_number = False
    else:
        if st.session_state.display == '0':
            st.session_state.display = char
        else:
            st.session_state.display += char

def clear_all():
    """Clear all calculator state"""
    st.session_state.display = '0'
    st.session_state.current_value = ''
    st.session_state.operator = None
    st.session_state.previous_value = ''
    st.session_state.new_number = True

def clear_entry():
    """Clear current entry"""
    st.session_state.display = '0'
    st.session_state.new_number = True

def calculate_basic():
    """Perform basic arithmetic operations"""
    try:
        if st.session_state.operator and st.session_state.previous_value != '':
            prev = safe_eval(st.session_state.previous_value)
            curr = safe_eval(st.session_state.display)
            
            if st.session_state.operator == '+':
                result = prev + curr
            elif st.session_state.operator == '-':
                result = prev - curr
            elif st.session_state.operator == '×':
                result = prev * curr
            elif st.session_state.operator == '÷':
                if curr == 0:
                    return "Error: Division by zero"
                result = prev / curr
            elif st.session_state.operator == '^':
                result = prev ** curr
            else:
                result = curr
            
            return result
        else:
            return safe_eval(st.session_state.display)
    except Exception as e:
        return "Error"

def set_operator(op):
    """Set operator for calculation"""
    st.session_state.previous_value = st.session_state.display
    st.session_state.operator = op
    st.session_state.new_number = True

def equals():
    """Calculate result"""
    result = calculate_basic()
    update_display(result)
    st.session_state.operator = None
    st.session_state.previous_value = ''
    st.session_state.new_number = True

def apply_function(func_name):
    """Apply scientific function"""
    try:
        value = safe_eval(st.session_state.display)
        
        if func_name == 'sin':
            if st.session_state.angle_mode == 'DEG':
                result = math.sin(math.radians(value))
            else:
                result = math.sin(value)
        elif func_name == 'cos':
            if st.session_state.angle_mode == 'DEG':
                result = math.cos(math.radians(value))
            else:
                result = math.cos(value)
        elif func_name == 'tan':
            if st.session_state.angle_mode == 'DEG':
                result = math.tan(math.radians(value))
            else:
                result = math.tan(value)
        elif func_name == 'sqrt':
            if value < 0:
                return "Error: Negative sqrt"
            result = math.sqrt(value)
        elif func_name == 'square':
            result = value ** 2
        elif func_name == 'cube':
            result = value ** 3
        elif func_name == 'log':
            if value <= 0:
                return "Error: Log of non-positive"
            result = math.log10(value)
        elif func_name == 'ln':
            if value <= 0:
                return "Error: Ln of non-positive"
            result = math.log(value)
        elif func_name == 'exp':
            result = math.exp(value)
        elif func_name == '1/x':
            if value == 0:
                return "Error: Division by zero"
            result = 1 / value
        elif func_name == 'abs':
            result = abs(value)
        elif func_name == 'factorial':
            if value < 0 or value != int(value):
                return "Error: Invalid factorial"
            result = math.factorial(int(value))
        elif func_name == 'asin':
            if value < -1 or value > 1:
                return "Error: Domain error"
            result = math.asin(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
        elif func_name == 'acos':
            if value < -1 or value > 1:
                return "Error: Domain error"
            result = math.acos(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
        elif func_name == 'atan':
            result = math.atan(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
        elif func_name == '10^x':
            result = 10 ** value
        elif func_name == 'negate':
            result = -value
        else:
            result = value
        
        update_display(result)
        st.session_state.new_number = True
    except Exception as e:
        update_display(f"Error")
        st.session_state.new_number = True

def toggle_angle_mode():
    """Toggle between DEG and RAD"""
    if st.session_state.angle_mode == 'DEG':
        st.session_state.angle_mode = 'RAD'
    else:
        st.session_state.angle_mode = 'DEG'

def memory_add():
    """Add current display to memory"""
    st.session_state.memory += safe_eval(st.session_state.display)

def memory_subtract():
    """Subtract current display from memory"""
    st.session_state.memory -= safe_eval(st.session_state.display)

def memory_recall():
    """Recall memory value"""
    update_display(st.session_state.memory)
    st.session_state.new_number = True

def memory_clear():
    """Clear memory"""
    st.session_state.memory = 0

# Calculator UI
st.markdown('<div class="calculator-body">', unsafe_allow_html=True)

st.markdown("<h1>CASIO fx-991 SCIENTIFIC CALCULATOR</h1>", unsafe_allow_html=True)

# Display
st.markdown(f"""
<div class="calculator-display">
    <div style="text-align: right; font-size: 14px; color: #2c3e50; margin-bottom: 5px;">
        {st.session_state.angle_mode} | M: {st.session_state.memory if st.session_state.memory != 0 else ''}
    </div>
    <div class="display-text">{st.session_state.display}</div>
</div>
""", unsafe_allow_html=True)

# Button layout
col1, col2, col3, col4, col5 = st.columns(5)

# Row 1 - Memory and mode functions
with col1:
    if st.button("AC", key="ac", use_container_width=True):
        clear_all()
        st.rerun()
with col2:
    if st.button("DEL", key="del", use_container_width=True):
        if len(st.session_state.display) > 1:
            st.session_state.display = st.session_state.display[:-1]
        else:
            st.session_state.display = '0'
        st.rerun()
with col3:
    if st.button(f"{st.session_state.angle_mode}", key="mode", use_container_width=True):
        toggle_angle_mode()
        st.rerun()
with col4:
    if st.button("M+", key="m_add", use_container_width=True):
        memory_add()
        st.rerun()
with col5:
    if st.button("M-", key="m_sub", use_container_width=True):
        memory_subtract()
        st.rerun()

# Row 2 - Scientific functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("sin", key="sin", use_container_width=True):
        apply_function('sin')
        st.rerun()
with col2:
    if st.button("cos", key="cos", use_container_width=True):
        apply_function('cos')
        st.rerun()
with col3:
    if st.button("tan", key="tan", use_container_width=True):
        apply_function('tan')
        st.rerun()
with col4:
    if st.button("x²", key="square", use_container_width=True):
        apply_function('square')
        st.rerun()
with col5:
    if st.button("x³", key="cube", use_container_width=True):
        apply_function('cube')
        st.rerun()

# Row 3 - More scientific functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("sin⁻¹", key="asin", use_container_width=True):
        apply_function('asin')
        st.rerun()
with col2:
    if st.button("cos⁻¹", key="acos", use_container_width=True):
        apply_function('acos')
        st.rerun()
with col3:
    if st.button("tan⁻¹", key="atan", use_container_width=True):
        apply_function('atan')
        st.rerun()
with col4:
    if st.button("√", key="sqrt", use_container_width=True):
        apply_function('sqrt')
        st.rerun()
with col5:
    if st.button("xʸ", key="power", use_container_width=True):
        set_operator('^')
        st.rerun()

# Row 4 - Logarithmic functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("log", key="log", use_container_width=True):
        apply_function('log')
        st.rerun()
with col2:
    if st.button("ln", key="ln", use_container_width=True):
        apply_function('ln')
        st.rerun()
with col3:
    if st.button("eˣ", key="exp", use_container_width=True):
        apply_function('exp')
        st.rerun()
with col4:
    if st.button("10ˣ", key="10pow", use_container_width=True):
        apply_function('10^x')
        st.rerun()
with col5:
    if st.button("n!", key="fact", use_container_width=True):
        apply_function('factorial')
        st.rerun()

# Row 5 - Number pad row 1
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("MR", key="mr", use_container_width=True):
        memory_recall()
        st.rerun()
with col2:
    if st.button("7", key="7", use_container_width=True):
        append_to_display('7')
        st.rerun()
with col3:
    if st.button("8", key="8", use_container_width=True):
        append_to_display('8')
        st.rerun()
with col4:
    if st.button("9", key="9", use_container_width=True):
        append_to_display('9')
        st.rerun()
with col5:
    if st.button("÷", key="div", use_container_width=True):
        set_operator('÷')
        st.rerun()

# Row 6 - Number pad row 2
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("MC", key="mc", use_container_width=True):
        memory_clear()
        st.rerun()
with col2:
    if st.button("4", key="4", use_container_width=True):
        append_to_display('4')
        st.rerun()
with col3:
    if st.button("5", key="5", use_container_width=True):
        append_to_display('5')
        st.rerun()
with col4:
    if st.button("6", key="6", use_container_width=True):
        append_to_display('6')
        st.rerun()
with col5:
    if st.button("×", key="mul", use_container_width=True):
        set_operator('×')
        st.rerun()

# Row 7 - Number pad row 3
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("1/x", key="inv", use_container_width=True):
        apply_function('1/x')
        st.rerun()
with col2:
    if st.button("1", key="1", use_container_width=True):
        append_to_display('1')
        st.rerun()
with col3:
    if st.button("2", key="2", use_container_width=True):
        append_to_display('2')
        st.rerun()
with col4:
    if st.button("3", key="3", use_container_width=True):
        append_to_display('3')
        st.rerun()
with col5:
    if st.button("-", key="sub", use_container_width=True):
        set_operator('-')
        st.rerun()

# Row 8 - Bottom row
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("π", key="pi", use_container_width=True):
        update_display(math.pi)
        st.session_state.new_number = True
        st.rerun()
with col2:
    if st.button("0", key="0", use_container_width=True):
        append_to_display('0')
        st.rerun()
with col3:
    if st.button(".", key="dot", use_container_width=True):
        if '.' not in st.session_state.display:
            append_to_display('.')
        st.rerun()
with col4:
    if st.button("=", key="eq", use_container_width=True):
        equals()
        st.rerun()
with col5:
    if st.button("+", key="add", use_container_width=True):
        set_operator('+')
        st.rerun()

# Constants row
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("e", key="e", use_container_width=True):
        update_display(math.e)
        st.session_state.new_number = True
        st.rerun()
with col2:
    if st.button("|x|", key="abs", use_container_width=True):
        apply_function('abs')
        st.rerun()
with col3:
    if st.button("(−)", key="neg", use_container_width=True):
        apply_function('negate')
        st.rerun()
with col4:
    if st.button("Ans", key="ans", use_container_width=True):
        # Display last answer (current display)
        st.rerun()
with col5:
    if st.button("EXP", key="exp_not", use_container_width=True):
        if 'e' not in st.session_state.display:
            append_to_display('e')
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
---
<div style='text-align: center; color: #ecf0f1; font-size: 12px;'>
    <b>Casio fx-991 Scientific Calculator</b><br>
    Full-featured scientific calculator with trigonometric, logarithmic, and statistical functions
</div>
""", unsafe_allow_html=True)
