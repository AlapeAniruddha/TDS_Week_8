import streamlit as st

num_1 = st.number_input("The first number",min_value=-30000,max_value=0,step=1)
num_2 = st.number_input("The second number",min_value=-20000,max_value=400000 ,step=1)
num_3 = st.number_input("The third number",min_value=0,max_value=20,step=1)

if num_1 > num_2 and num_1 > num_3:
    st.write('num_1')
elif num_2 > num_3 and num_2 > num_1:
    st.write('num_2')
elif num_3 > num_2 and num_3 > num_1:
    st.write('num_3')    
else: 
    st.write('Equal numbers')  
