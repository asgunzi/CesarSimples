# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 01:33:36 2024

@author: ASGUNZI
"""

import streamlit as st


def cifrarCesar(mensagem, chave):
    
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    alfnovo =alfabeto[chave:] + alfabeto[:chave]
    
    #Cria um dicionário
    dicAlfabeto ={}
    for k in range(len(alfabeto)):
        dicAlfabeto[alfabeto[k]] = alfnovo[k]
        
    
    #Só para conferir o alfabeto novo    
    #print(alfnovo)
    
    msgOut =""
    
    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    for ch in msg2:
        if ch in alfabeto:
            msgOut += dicAlfabeto[ch]
        else:
            msgOut += ch
    
    return(msgOut)
    
    
def decifrarCesar(mensagem, chave):
    
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    alfnovo =alfabeto[chave:] + alfabeto[:chave]
    
    #Cria um dicionário
    dicAlfabeto ={}
    for k in range(len(alfabeto)):
        dicAlfabeto[alfnovo[k]] = alfabeto[k]
    #Aqui a chave é oposta. Tenho alfnovo e quero o alfabeto original
    
    
    msgOut =""
    
    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    for ch in msg2:
        if ch in alfnovo:
            msgOut += dicAlfabeto[ch]
        else:
            msgOut += ch
    
    return(msgOut)


#st.image("ForgottenMath.png")
st.image("https://ideiasesquecidas.com/wp-content/uploads/2024/07/forgottenmath.png")

st.title("Exemplo - Cifra de César simples")

col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    nkey = st.selectbox("Selecione a chave:", list(range(1, 27)))

user_input = st.text_input("Entre texto a cifrar:")

# Check if the input is not empty
if user_input:
    # Cifrar mensagem

    msgCifrada = cifrarCesar( user_input, nkey)
    
    # Display the reversed text
    st.write("Mensagem cifrada:")
    st.write(msgCifrada)
    
#Marca separatória
st.markdown("---")

user_input2 = st.text_input("Entre texto a decifrar:")

# Check if the input is not empty
if user_input2:
    # Decifrar mensagem

    msgDecifrada = decifrarCesar( user_input2, nkey)
    
    # Display the reversed text
    st.write("Mensagem decifrada:")
    st.write(msgDecifrada)
    
    
