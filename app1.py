import streamlit as st

st.title("The Echo")
st.write("A simple echo device")

name = st.text_input("Enter your name")
message = st.text_input("Enter your message")

tk_count = len(message) * 4

if st.button("Transmit", use_container_width=True):
    if name == "":
        st.error("Name is empty")
    elif message == "":
        st.warning("Provide a message to transmit")
    else:
        st.success(f"Transmission success! Greetings {name}. We received your message: {message}")
        st.info(f"Your message will consume approximately {tk_count} tokens")

