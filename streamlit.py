import streamlit as st

st.write("""
# Largest number identifier
This app identifies the largest of the given three numbers
""")

num_1 = st.number_input("Enter the first number",step=1)
num_2 = st.number_input("Enter the second number",step=1)
num_3 = st.number_input("Enter the third number",step=1)

def largest_num(num_1,num_2,num_3):
    if num_1 > num_2 and num_1 > num_3:
        st.write('The largest number is the first number = ',num_1)
    elif num_2 > num_3 and num_2 > num_1:
        st.write('The largest number is the second number = ',num_2)
    elif num_3 > num_2 and num_3 > num_1:
        st.write('The largest number is the third number = ',num_3)    
    elif num_3 == num_2 and num_3 == num_1:
        st.write('All the numbers are equal and the value is = ',num_3)
    elif num_3 == num_2 and num_3 != num_1: 
        st.write('Two numbers are equal and the value is = ',num_3)  
    elif num_1 == num_2 and num_3 != num_1: 
        st.write('Two numbers are equal and the value is = ',num_1)  
    elif num_3 == num_1 and num_3 != num_2: 
        st.write('Two numbers are equal and the value is = ',num_3)  

if st.button('Find Largest'):
    largest_num(num_1,num_2,num_3)

        
        
