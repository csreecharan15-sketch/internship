import streamlit as st

st.title("Calculator")

if "calculate" not in st.session_state:
    st.session_state.calculate = ""

st.text_input("Calculate", value=st.session_state.calculate, disabled=True)

buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3"
]

col_ops = st.columns(4)
ops = ["+", "-", "*", "/"]
for i, op in enumerate(ops):
    with col_ops[i]:
        if st.button(op, key = f"op_{op}", use_container_width = True):
            st.session_state.calculate += op
            st.rerun()

index = 0
for row in range(3):
    cols = st.columns(3)
    for col in cols:
        char = buttons[index]
        with col:
            if st.button(char, key = f"btn_{char}", use_container_width = True):
                st.session_state.calculate += char
                st.rerun()
        index += 1

if st.button("0", key = "btn_0", use_container_width = True):
    st.session_state.calculate += str(0)
    st.rerun()

clear, equal = st.columns(2)

with clear:
    if st.button("Clear", key = "clear", use_container_width=True):
        st.session_state.calculate = ""
        st.rerun()

with equal:
    if st.button("=", key = "equal", use_container_width=True):
        try:
            if st.session_state.calculate:
                result = eval(st.session_state.calculate)
                st.session_state.calculate = str(result)
        except ZeroDivisionError:
            st.session_state.calculate = "ERROR"
        except Exception:
            st.session_state.calculate = "ERROR"
        st.rerun()
