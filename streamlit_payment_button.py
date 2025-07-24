
import streamlit as st
import requests
import webbrowser

st.header("💳 Unlock Lifetime Access")

st.markdown("""
Enjoy full access to Stack Tracker:
- Unlimited session logging
- Tax-ready PDF exports
- Comp tracking
- One-time payment — no subscription

**Price: $9.99**
""")

if st.button("Buy Now with Stripe"):
    response = requests.post("http://localhost:4242/create-checkout-session")
    if response.status_code == 200:
        checkout_url = response.json().get("url")
        st.success("Redirecting to checkout...")
        webbrowser.open(checkout_url)
    else:
        st.error("Failed to initiate payment. Please try again.")
