import streamlit as st
from Feature_01 import return_even 

original_list = [i for i in range(10)]

even_list = return_even(original_list)

st.write ('Hello Sofiya and Valentin')

st.write (even_list)

st.write ('love')

st.write ('love you too')