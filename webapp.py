import streamlit as st
import BintoDec as bd


def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary = bin(decimal).replace("0b", "")
    return binary

st.title('Binary and Decimal Converter')

conversion_type = st.selectbox('Choose conversion type:', ('Binary to Decimal', 'Decimal to Binary'))

if conversion_type == 'Binary to Decimal':
    binary_input = st.text_input('Enter a binary number:', value='', max_chars=None, key="binary_number", type='default')
    if st.button('Convert to Decimal'):
        if all([bit in ['0', '1'] for bit in binary_input]):
            decimal_output =bd.BinToDecimal(int(binary_input))
            st.write('Decimal:', decimal_output)
        else:
            st.write('Please enter a valid binary number.')
else:
    decimal_input = st.text_input('Enter a decimal number:', value='', max_chars=None, key=None, type='default')
    if st.button('Convert to Binary'):
        if decimal_input.isdigit():
            binary_output = decimal_to_binary(decimal_input)
            st.write('Binary:', binary_output)
        else:
            st.write('Please enter a valid decimal number.')
