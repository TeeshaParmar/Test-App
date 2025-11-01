# app.py
import streamlit as st
import math

# -------- PAGE CONFIG ----------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# -------- CSS (white background, clean look) ----------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
            text-align: center;
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
        }
        .calculator {
            background-color: #f6f7f9;
            padding: 18px;
            border-radius: 12px;
            width: 360px;
            margin: 18px auto;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }
        .stTextInput>div>div>input {
            text-align: right;
            background-color: #ffffff;
            color: #000000;
            font-size: 1.4rem;
            border-radius: 8px;
            height: 56px;
            border: 1.5px solid #d0d7de;
        }
        .stButton>button {
            width: 64px;
            height: 48px;
            margin: 4px;
