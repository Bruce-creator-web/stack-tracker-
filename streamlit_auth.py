
import streamlit as st

# Simulated user database (replace with a real DB in production)
user_db = {
    "bryce@example.com": "securepass123",  # example user
}

st.header("🔐 Login to Stack Tracker")

# If not logged in, show login form
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")

        if login:
            if email in user_db and user_db[email] == password:
                st.session_state.authenticated = True
                st.session_state.user = email
                st.success("Login successful!")
            else:
                st.error("Invalid credentials")

# If logged in, greet user
if st.session_state.authenticated:
    st.success(f"Welcome, {st.session_state.user} 👋")
    if st.button("Log Out"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.experimental_rerun()
