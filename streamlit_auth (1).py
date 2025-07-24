
import streamlit as st

# Simulated user database (in-memory for now)
if 'user_db' not in st.session_state:
    st.session_state.user_db = {
        "bryce@example.com": "securepass123"  # example default user
    }

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "login"

st.title("🔐 Stack Tracker - Account Access")

if st.session_state.auth_mode == "login":
    st.subheader("Login")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Log In")

        if login:
            if email in st.session_state.user_db and st.session_state.user_db[email] == password:
                st.session_state.authenticated = True
                st.session_state.user = email
                st.success(f"Welcome back, {email}!")
            else:
                st.error("Invalid credentials")

    if st.button("Don't have an account? Sign Up"):
        st.session_state.auth_mode = "signup"

elif st.session_state.auth_mode == "signup":
    st.subheader("Create Account")
    with st.form("signup_form"):
        new_email = st.text_input("New Email")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        signup = st.form_submit_button("Sign Up")

        if signup:
            if new_password != confirm_password:
                st.error("Passwords do not match")
            elif new_email in st.session_state.user_db:
                st.error("Email already registered")
            else:
                st.session_state.user_db[new_email] = new_password
                st.success("Account created! You can now log in.")
                st.session_state.auth_mode = "login"

    if st.button("Already have an account? Log In"):
        st.session_state.auth_mode = "login"

# Logged in state
if st.session_state.authenticated:
    st.success(f"Logged in as {st.session_state.user}")
    if st.button("Log Out"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.auth_mode = "login"
        st.experimental_rerun()
