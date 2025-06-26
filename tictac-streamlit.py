import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe with Streamlit", page_icon="👾", layout="wide")
st.title("Tic Tac Toe | You VS Computer")
st.write("Let's Start")
st.sidebar.success("Hy Everyone , This is my first project with Streamlit . Please play this simple game and have a good day ! \n\n Tashika")

if "board" not in st.session_state:
    st.session_state.board=["" for _ in range(9)]
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
    st.session_state.board=["" for _ in range(9)]
    st.session_state.player="X"
    st.session_state.winner=None

def max_min(board,is_maximum):
    winner=check_winner(board)
    if winner=="0":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0
    
    if(is_maximum):
        best_score=-float("inf")
        for i in range(9):
            if board[i]=="":
                board[i]="O"
                score= max_min(board,False)
                board[i]=""
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=float("inf")
        for i in range(9):
            if board[i]=="":
                board[i]="X"
                score= max_min(board,True)
                board[i]=""
                best_score=max(score,best_score)
        return best_score
 
if st.session_state.winner():
    if st.session_state.winner == "Draw" :
        st.succes("It's a draw 🤝 ")
    else:
        st.success(f"Player {st.session_state.winner} wins🏆")    
    st.button("Play again", onclick=reset_game())
else:
    st.info("Your Turn (X). You'll go first.")   
