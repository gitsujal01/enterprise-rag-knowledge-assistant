import streamlit as st

# Users dictionary (username: password + role)
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"},
    "user2": {"password": "user234", "role": "user"},
}

def login(username, password):
    """
    Login function without pandas.
    Sets Streamlit session_state for logged_in, username, and role.
    """
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

    if username in USERS and USERS[username]["password"] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = USERS[username]["role"]
        st.success(f"Logged in as {username} ({st.session_state.role})")
        return True
    else:
        st.error("Invalid username or password")
        return False