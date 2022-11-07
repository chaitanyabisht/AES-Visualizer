from AES import AES
import copy
import streamlit as st
import numpy as np

@st.cache
def generate_random_key():
    k = np.random.randint(0, 16, size=32)
    k = ''.join([str(hex(i))[2:] for i in k])
    return k

def set_state_from_ascii(cipher, ascii):
    if (len(ascii) > 16): # If the string is too long, truncate it
        ascii = ascii[0:16]
    if (len(ascii) < 16): # If the string is too short, pad it with PKCS#7
        # Pad using PKCS7
        ascii = ascii + (16 - len(ascii)) * chr(16 - len(ascii))
    state = []

    # Converting the string into its ascii values and storing it in a list
    for i in range(0, 4):
        lst = [ord(ascii[i*4]), ord(ascii[i*4+1]), ord(ascii[i*4+2]), ord(ascii[i*4+3])]
        state.append(lst)

    # transpose the state to column major   
    state = [[row[i] for row in state] for i in range(len(state[0]))]
    cipher.set_state((state))

@st.cache
def key_matrix(key):
    k_mat = []
    row = []
    for i in range(0, len(key), 2):
        row.append(key[i:i+2])
        if (len(row) == 4):
            k_mat.append(copy.deepcopy(row))
            row = []
    # transpose the matrix
    k_mat = [[row[i] for row in k_mat] for i in range(len(k_mat[0]))]
    k_mat = [[int(i, 16) for i in row] for row in k_mat]
    return k_mat

@st.cache
def round_keys(key):
    # convert the key into column major matrix
    k_mat = key_matrix(key)
    cipher = AES(k_mat)
    return cipher.key_expansion()

@st.cache
def latex_table(obj):
    table = r'''$ \begin{bmatrix}''' + '\n'
    for i in range(0, 4):
        for j in range(0, 4):
            # pad the hex value with 0s
            table += hex(obj[i][j])[2:].zfill(2) + ''' & '''
        table = table[:-2] + r'\\' + '\n'
    table = table[:-1] + '\n' +r'''\end{bmatrix} $'''
    return table

@st.cache
def get_key_expansion(round, key):
    cipher = AES(key_matrix(key))
    sub_round_keys = cipher.key_expansion_steps(round)
    return sub_round_keys

def encryption_round(message, key, round):
    cipher = AES(key_matrix(key))
    set_state_from_ascii(cipher, message)
    round_steps = cipher.get_round_steps()
    # round_steps = cipher.get_round_steps()
    return round_steps[round]

if __name__ == '__main__':
    # key = '2b7e151628aed2a6abf7158809cf4f3c'
    # r = (round_keys(key))
    # for i in range(11):
    #     print('Round', i)
    #     AES.pretty_print(r[i])
    #     print()
    r = round_keys('2b7e151628aed2a6abf7158809cf4f3c')
    print('Round 0')
    print(latex_table(r[0]))