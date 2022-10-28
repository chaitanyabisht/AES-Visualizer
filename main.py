import streamlit as st
import pandas as pd
import numpy as np
from utils import *

st.title('AES Visualizer')
st.subheader('A web app to visualize the AES-128 encryption algorithm')

message = st.text_input('Enter a message in ASCII', placeholder='Enter a message')
key = st.empty()
key.text_input('Enter a 128-bit key in hex', placeholder='Enter a key')
random_key = st.checkbox('Generate a random key', value=True)
k = 0

if random_key:
    k = generate_random_key()
    key.text_input('Enter a 128-bit key in hex', k)

option = st.selectbox(
    'What would you like to see?',
    ('Please select','Round Keys', 'Key Expansion', 'Encryption Round'))

if option == 'Round Keys':
    st.write('Round Keys')
    round_keys = round_keys(k)
    col1, col2 = st.columns(2)
    with col1:
        for i in range(11):
            if (i % 2 == 0):
                st.write('Round', i)
                st.write(str(latex_table(round_keys[i])))
                st.write()
    with col2:
        for i in range(11):
            if (i % 2 == 1):
                st.write('Round', i)
                st.write(str(latex_table(round_keys[i])))
                st.write()
elif option == 'Key Expansion':
    st.write('Key Expansion')
    round = st.slider('Select a round', 1, 10, 1)
    sub_round_keys = get_key_expansion(round, k)

    st.write('Initial Key')
    st.write(str(latex_table(sub_round_keys[0])))
    st.write()

    st.write('Take last column of previous key and move top byte to bottom')
    st.write(str(latex_table(sub_round_keys[1])))
    st.write()

    st.write('Substitute each byte of the last column with the corresponding byte in the S-Box')
    st.write(str(latex_table(sub_round_keys[2])))
    st.write()

    st.write('XOR the top byte of the last column with the corresponding byte in the Round Constant Table')
    st.write(str(latex_table(sub_round_keys[3])))
    st.write()

    st.write('XOR the first column of the new key with the last column of the previous key')
    st.write(str(latex_table(sub_round_keys[4])))
    st.write()

    st.write('XOR the remaining columns of the new key with the corresponding columns of the previous key')
    st.write(str(latex_table(sub_round_keys[5])))
    st.write()


elif option == 'Encryption Round':
    st.write('Encryption Round')
    round = st.slider('Select a round', 1, 10, 1)
    round_steps = encryption_round(message, k, round)

    st.write('Initial State')
    st.write(str(latex_table(round_steps[0])))
    st.write()
    if (round == 1):
        st.write('Add Round Key')
        st.write(str(latex_table(round_steps[1])))
        st.write()

        st.write('Substitute Bytes')
        st.write(str(latex_table(round_steps[2])))
        st.write()

        st.write('Shift Rows')
        st.write(str(latex_table(round_steps[3])))
        st.write()

        st.write('Mix Columns')
        st.write(str(latex_table(round_steps[4])))
        st.write()

        st.write('Add Round Key')
        st.write(str(latex_table(round_steps[5])))
        st.write()
    elif (round == 10):
        st.write('Substitute Bytes')
        st.write(str(latex_table(round_steps[1])))
        st.write()

        st.write('Shift Rows')
        st.write(str(latex_table(round_steps[2])))
        st.write()

        st.write('Add Round Key')
        st.write(str(latex_table(round_steps[3])))
        st.write()
    else:
        st.write('Substitute Bytes')
        st.write(str(latex_table(round_steps[1])))
        st.write()

        st.write('Shift Rows')
        st.write(str(latex_table(round_steps[2])))
        st.write()

        st.write('Mix Columns')
        st.write(str(latex_table(round_steps[3])))
        st.write()

        st.write('Add Round Key')
        st.write(str(latex_table(round_steps[4])))
        st.write()
elif option == 'Please select':
    st.write('Please select an option')