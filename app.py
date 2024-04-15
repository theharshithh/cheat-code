import time
import streamlit as st
import os


if st.button('clear'):
    st.session_state.first_key = ''
    st.session_state.second = ''
    st.session_state.ques = ''

def find_program(ques):
    directory = 'dataset'
    file_names = os.listdir(directory)
    for file_name in file_names:
        if ques in file_name:
            st.image(os.path.join(directory, file_name))

pass_key = st.text_input('Enter the key (needed for py)', type='password', label_visibility="hidden", key='first_key')
ques = st.text_input('Enter the problem', type='password', key='ques', label_visibility="hidden")



if ques != '':
    if pass_key ==  'pypip' or 'HKM':                
        find_program(ques)



