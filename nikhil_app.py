import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Zerodha API Website", layout="wide")

# Title and Introduction
st.title("My Zerodha API Website")
st.header("Welcome to my website!")
st.write("This website demonstrates my Zerodha API application.")

# Contact Form
with st.form("contact_form"):
    st.subheader("Get in Touch")
    name = st.text_input("Name", placeholder="Your Name")
    email = st.text_input("Email", placeholder="your@email.com")
    message = st.text_area("Message", height=100)
    submitted = st.form_submit_button("Submit")

# Conditional statement to handle form submission
if submitted:
    st.success("Thank you for contacting me!")
    # Add notification or email sending functionality here

# Sidebar
with st.sidebar:
    st.header("About Me")
    st.info("I'm Nikhil a trader and developer.")
    st.write("Connect with me:")
    st.button("LinkedIn")
    st.button("Twitter")
    st.button("GitHub")

# Additional Sections (optional)
st.header("My Projects")
st.write("Coming soon...")

st.header("Blog")
st.write("Coming soon...")
