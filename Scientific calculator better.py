import streamlit as st
import math

# --- PAGE CONFIG ---
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .calculator {
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 12px;
            width: 340px;
            margin: auto;
            box-shadow: 0 0 15px rgba(0,0,0,0.15);
        }
        .stTextInput > div > div > input {
            text-align: right;
            background-color: #ffffff;
            color: #000000;
            font-size: 1.5em;
            border-radius: 8px;
            height: 50px;
            border: 2px solid #ccc;
        }
        .stButton > button {
            width: 65px;
            height: 50px;
            margin: 4px;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            border: none;
            color: white;
            background-color: #0078D4;
            transition: 0.2s;
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

st.markdown("<h2 style='text-align:center;'>🧮 Scientific Calculator</h2>", unsafe_allow_html=True)

# --- STATE ---
if "expression"
