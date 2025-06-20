import streamlit as st
from xgboost_predictor import get_stock_predictions

st.set_page_config(page_title="Breakout Signal Dashboard", page_icon="📈", layout="wide")

st.title("📈 Breakout Signal Dashboard")

try:
    predictions = get_stock_predictions()
    if predictions:
        st.success("Breakout signals generated successfully!")
        for pred in predictions:
            st.write(pred)
    else:
        st.warning("No breakout signals today.")
except Exception as e:
    st.error(f"Error: {e}")
