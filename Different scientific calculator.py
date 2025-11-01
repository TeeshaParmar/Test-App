import streamlit as st
import math
import numpy as np

# Page configuration
st.set_page_config(page_title="Casio fx-991 Calculator", layout="centered")

# Custom CSS for vibrant purple-yellow tropical theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a0033 0%, #2d1b4e 25%, #4a2c6d 50%, #2d1b4e 75%, #1a0033 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 20px;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stButton > button {
        width: 100%;
        height: 50px;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid #6a1b9a;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        background: linear-gradient(145deg, #4a148c, #6a1b9a);
        color: #fff;
        font-family: 'Orbitron', sans-serif;
        box-shadow: 0 4px 15px rgba(106, 27, 154, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 235, 59, 0.6), 0 0 30px rgba(255, 235, 59, 0.3);
        background: linear-gradient(145deg, #6a1b9a, #8e24aa);
        border-color: #ffeb3b;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.5rem;
    }
    
    .calculator-display {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 25px;
        border-radius: 15px;
        border: 3px solid #ffeb3b;
        margin-bottom: 25px;
        box-shadow: 
            0 0 30px rgba(255, 235, 59, 0.5),
            inset 0 2px 10px rgba(0,0,0,0.5),
            0 8px 32px rgba(106, 27, 154, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .calculator-display::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(255, 235, 59, 0.1),
            transparent
        );
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .expression-text {
        font-family: 'Orbitron', monospace;
        font-size: 16px;
        color: #ffeb3b;
        text-align: right;
        min-height: 25px;
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(255, 235, 59, 0.8);
        position: relative;
        z-index: 1;
    }
    
    .display-text {
        font-family: 'Orbitron', monospace;
        font-size: 32px;
        font-weight: bold;
        color: #fff;
        text-align: right;
        min-height: 45px;
        word-wrap: break-word;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8), 0 0 30px rgba(255, 235, 59, 0.6);
        position: relative;
        z-index: 1;
    }
    
    .calculator-body {
        background: linear-gradient(135deg, #2d1b4e 0%, #4a148c 50%, #2d1b4e 100%);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 
            0 20px 60px rgba(0,0,0,0.6),
            0 0 40px rgba(255, 235, 59, 0.3),
            inset 0 1px 0 rgba(255, 235, 59, 0.2);
        border: 2px solid #6a1b9a;
        position: relative;
    }
    
    .calculator-body::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 30%, rgba(255, 235, 59, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(142, 36, 170, 0.2) 0%, transparent 50%);
        border-radius: 20px;
        pointer-events: none;
    }
    
    h1 {
        color: #ffeb3b;
        text-align: center;
        font-size: 22px;
        margin-bottom: 15px;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 
            0 0 10px rgba(255, 235, 59, 0.8),
            0 0 20px rgba(255, 235, 59, 0.6),
            0 0 30px rgba(255, 235, 59, 0.4);
        letter-spacing: 2px;
        animation: glow 2s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px rgba(255, 235, 59, 0.8), 0 0 20px rgba(255, 235, 59, 0.6); }
        50% { text-shadow: 0 0 20px rgba(255, 235, 59, 1), 0 0 30px rgba(255, 235, 59, 0.8), 0 0 40px rgba(255, 235, 59, 0.6); }
    }
    
    .mode-indicator {
        display: inline-block;
        padding: 4px 12px;
        background: linear-gradient(135deg, #ffeb3b, #fdd835);
        color: #1a0033;
        border-radius: 12px;
        font-weight: bold;
        font-size: 12px;
        margin-right: 10px;
        box-shadow: 0 0 15px rgba(255, 235, 59, 0.6);
        font-family: 'Orbitron', sans-serif;
    }
    
    .memory-indicator {
        display: inline-block;
        color: #ffeb3b;
        font-size: 12px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 235, 59, 0.8);
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Special button styles */
    [data-testid="stButton"]:has(button[key="eq"]) button {
        background: linear-gradient(145deg, #fdd835, #ffeb3b);
        color: #1a0033;
        font-size: 24px;
        border: 3px solid #fff59d;
    }
    
    [data-testid="stButton"]:has(button[key="eq"]) button:hover {
        background: linear-gradient(145deg, #ffeb3b, #ffee58);
        box-shadow: 0 8px 30px rgba(255, 235, 59, 0.8), 0 0 50px rgba(255, 235, 59, 0.5);
    }
    
    [data-testid="stButton"]:has(button[key="ac"]) button {
        background: linear-gradient(145deg, #d32f2f, #f44336);
        border-color: #ff5252;
    }
    
    [data-testid="stButton"]:has(button[key="ac"]) button:hover {
        background: linear-gradient(145deg, #f44336, #e57373);
        box-shadow: 0 8px 25px rgba(244, 67, 54, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'expression' not in st.session_state:
    st.session_state.expression = ''
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
    st.session_state.angle_mode = 'DEG'

def safe_eval(value):
    """Safely evaluate mathematical expression"""
    try:
        return float(value)
    except:
        return 0

def format_number(num):
    """Format number for display"""
    try:
        if isinstance(num, str):
            return num
        if abs(num) < 1e-10 and num != 0:
            return f"{num:.2e}"
        if abs(num) > 1e10:
            return f"{num:.2e}"
        if num == int(num):
            return str(int(num))
        return str(round(num, 10)).rstrip('0').rstrip('.')
    except:
        return str(num)

def update_display(value, expr=''):
    """Update calculator display"""
    st.session_state.display = format_number(value)
    if expr:
        st.session_state.expression = expr

def append_to_display(char):
    """Append character to display"""
    if st.session_state.new_number:
        st.session_state.display = char
        st.session_state.new_number = False
    else:
        if st.session_state.display == '0' and char != '.':
            st.session_state.display = char
        else:
            st.session_state.display += char

def clear_all():
    """Clear all calculator state"""
    st.session_state.display = '0'
    st.session_state.expression = ''
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
                    return "Error: Div/0"
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
    current_display = st.session_state.display
    st.session_state.previous_value = current_display
    st.session_state.operator = op
    st.session_state.expression = f"{current_display} {op}"
    st.session_state.new_number = True

def equals():
    """Calculate result"""
    if st.session_state.operator and st.session_state.previous_value:
        full_expr = f"{st.session_state.expression} {st.session_state.display}"
        result = calculate_basic()
        st.session_state.expression = f"{full_expr} ="
        update_display(result)
        st.session_state.operator = None
        st.session_state.previous_value = ''
        st.session_state.new_number = True

def apply_function(func_name):
    """Apply scientific function"""
    try:
        value = safe_eval(st.session_state.display)
        orig_display = st.session_state.display
        
        if func_name == 'sin':
            if st.session_state.angle_mode == 'DEG':
                result = math.sin(math.radians(value))
            else:
                result = math.sin(value)
            expr = f"sin({orig_display})"
        elif func_name == 'cos':
            if st.session_state.angle_mode == 'DEG':
                result = math.cos(math.radians(value))
            else:
                result = math.cos(value)
            expr = f"cos({orig_display})"
        elif func_name == 'tan':
            if st.session_state.angle_mode == 'DEG':
                result = math.tan(math.radians(value))
            else:
                result = math.tan(value)
            expr = f"tan({orig_display})"
        elif func_name == 'sqrt':
            if value < 0:
                result = "Error: √neg"
                expr = f"√({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.sqrt(value)
            expr = f"√({orig_display})"
        elif func_name == 'square':
            result = value ** 2
            expr = f"({orig_display})²"
        elif func_name == 'cube':
            result = value ** 3
            expr = f"({orig_display})³"
        elif func_name == 'log':
            if value <= 0:
                result = "Error: log≤0"
                expr = f"log({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.log10(value)
            expr = f"log({orig_display})"
        elif func_name == 'ln':
            if value <= 0:
                result = "Error: ln≤0"
                expr = f"ln({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.log(value)
            expr = f"ln({orig_display})"
        elif func_name == 'exp':
            result = math.exp(value)
            expr = f"e^({orig_display})"
        elif func_name == '1/x':
            if value == 0:
                result = "Error: 1/0"
                expr = f"1/({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = 1 / value
            expr = f"1/({orig_display})"
        elif func_name == 'abs':
            result = abs(value)
            expr = f"|{orig_display}|"
        elif func_name == 'factorial':
            if value < 0 or value != int(value):
                result = "Error: fact"
                expr = f"({orig_display})!"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.factorial(int(value))
            expr = f"({int(value)})!"
        elif func_name == 'asin':
            if value < -1 or value > 1:
                result = "Error: domain"
                expr = f"sin⁻¹({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.asin(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
            expr = f"sin⁻¹({orig_display})"
        elif func_name == 'acos':
            if value < -1 or value > 1:
                result = "Error: domain"
                expr = f"cos⁻¹({orig_display})"
                update_display(result, expr)
                st.session_state.new_number = True
                return
            result = math.acos(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
            expr = f"cos⁻¹({orig_display})"
        elif func_name == 'atan':
            result = math.atan(value)
            if st.session_state.angle_mode == 'DEG':
                result = math.degrees(result)
            expr = f"tan⁻¹({orig_display})"
        elif func_name == '10^x':
            result = 10 ** value
            expr = f"10^({orig_display})"
        elif func_name == 'negate':
            result = -value
            expr = f"-({orig_display})"
        else:
            result = value
            expr = orig_display
        
        update_display(result, expr)
        st.session_state.new_number = True
    except Exception as e:
        update_display(f"Error", f"{func_name}")
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
    update_display(st.session_state.memory, f"MR: {format_number(st.session_state.memory)}")
    st.session_state.new_number = True

def memory_clear():
    """Clear memory"""
    st.session_state.memory = 0

# Calculator UI
st.markdown('<div class="calculator-body">', unsafe_allow_html=True)

st.markdown("<h1>⚡ CASIO fx-991 SCIENTIFIC CALCULATOR ⚡</h1>", unsafe_allow_html=True)

# Display with expression line
mem_display = f"M: {format_number(st.session_state.memory)}" if st.session_state.memory != 0 else ""
st.markdown(f"""
<div class="calculator-display">
    <div style="text-align: right; margin-bottom: 8px;">
        <span class="mode-indicator">{st.session_state.angle_mode}</span>
        <span class="memory-indicator">{mem_display}</span>
    </div>
    <div class="expression-text">{st.session_state.expression}</div>
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
        update_display(math.pi, "π")
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
        update_display(math.e, "e")
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
        st.rerun()
with col5:
    if st.button("EXP", key="exp_not", use_container_width=True):
        if 'e' not in st.session_state.display.lower():
            append_to_display('e')
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer with glowing effect
st.markdown("""
---
<div style='text-align: center; color: #ffeb3b; font-size: 14px; font-family: "Orbitron", sans-serif; text-shadow: 0 0 10px rgba(255, 235, 59, 0.8);'>
    <b>⚡ Casio fx-991 Scientific Calculator ⚡</b><br>
    <span style='color: #ce93d8; font-size: 12px;'>Advanced Scientific Computing with Expression Display</span>
</div>
""", unsafe_allow_html=True)
