import streamlit as st
import time

txt = "%"
my_bar = st.progress(0 , text = txt)
for pr in range(100):
    time.sleep(0.1)
    my_bar.progress(pr + 1 , text = str(pr))

with st.spinner("wait for it..."):
    time.sleep(5)
st.write("wait over")

st.balloons()

st.snow()

e = RuntimeError("Exp")
st.exception(e)
