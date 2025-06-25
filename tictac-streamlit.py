import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe with Streamlit", page_icon="👾", layout="wide")
st.title("Tic Tac Toe | You VS Computer")
st.write("Let's Start")
st.sidebar.success("Hy Everyone , This is my first project with Streamlit . Please play this simple game and have a good day ! \n\n Tashika")

if "board" not in st.session_state:
    st.session_state.board=[" for _ in range"]
    st.session_state.player="X"
    st.session_state.winner=None

def check_winner(board):
    wins =[(0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8),
            (0,4,8) , (2,4,6)]
    for a,b,c in wins:
        if board[a] and board[a]==board[b]==board[c]:
            return board[a]
        
    if all(cell != "" for cell in board):
        return "Draw"
            
    return None

def reset_game():
    st.session_state.board=[" for _ in range"]
    st.session_state.player="X"
    st.session_state.winner=None
