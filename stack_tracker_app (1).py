
import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state
if 'session_log' not in st.session_state:
    st.session_state.session_log = pd.DataFrame(columns=["Date", "Casino", "BuyIn", "CashOut", "Comps", "Notes"])

st.title("🎰 Stack Tracker")
st.subheader("Know when to cash out — not burn out.")

# Add new session
st.header("➕ Add Gambling Session")
with st.form("session_form"):
    date = st.date_input("Date", value=datetime.today())
    casino = st.text_input("Casino")
    buy_in = st.number_input("Buy-in Amount", min_value=0)
    cash_out = st.number_input("Cash-out Amount", min_value=0)
    comps = st.number_input("Comps Value ($)", min_value=0)
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Add Session")

    if submitted:
        new_entry = pd.DataFrame([{
            "Date": pd.to_datetime(date),
            "Casino": casino,
            "BuyIn": buy_in,
            "CashOut": cash_out,
            "Comps": comps,
            "Notes": notes
        }])
        st.session_state.session_log = pd.concat([st.session_state.session_log, new_entry], ignore_index=True)
        st.success("Session added successfully!")

# Display session history
st.header("📅 Session Log")
st.dataframe(st.session_state.session_log)

# Summary
st.header("📊 Summary")
wins = st.session_state.session_log[st.session_state.session_log["CashOut"] > st.session_state.session_log["BuyIn"]]["CashOut"].sum()
losses = st.session_state.session_log[st.session_state.session_log["CashOut"] < st.session_state.session_log["BuyIn"]]["BuyIn"].sum()
net_profit = st.session_state.session_log["CashOut"].sum() - st.session_state.session_log["BuyIn"].sum()
estimated_tax = wins - losses
comps_total = st.session_state.session_log["Comps"].sum()

st.metric("Total Wins", f"${wins:,.2f}")
st.metric("Total Losses", f"${losses:,.2f}")
st.metric("Net Profit", f"${net_profit:,.2f}")
st.metric("Estimated Taxable Income", f"${estimated_tax:,.2f}")
st.metric("Total Comps Earned", f"${comps_total:,.2f}")
