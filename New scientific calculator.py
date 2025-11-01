# app.py
import streamlit as st
import math
import ast
import operator

# ---------- Config ----------
st.set_page_config(page_title="Scientific Calculator (Casio-style)", page_icon="🧮", layout="centered")

st.markdown(
    """
    <div style="text-align:center">
      <h2 style="margin-bottom:0.1rem">🔢 Scientific Calculator (Casio-style)</h2>
      <div style="color:gray; font-size:0.9rem">Safe evaluation — supports sin, cos, tan, ln, log, sqrt, factorial, π, e, ^, %</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Session state ----------
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Safe evaluator using AST ----------
# Allowed operators mapping
_allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
}

# Allowed names (functions/constants)
_allowed_names = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,         # natural log
    "log": math.log10,      # log base 10
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "fact": math.factorial, # use fact(n) for factorial
}

def _eval_node(node):
    """Recursively evaluate an AST node with strict rules."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)

    # Numbers
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Unsupported constant type")

    # Binary operations
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in _allowed_operators:
            return _allowed_operators[op_type](left, right)
        else:
            raise ValueError(f"Operator {op_type} not allowed")

    # Unary operations (+/-)
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type in _allowed_operators:
            return _allowed_operators[op_type](operand)
        else:
            raise V
