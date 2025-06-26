import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe with Streamlit", page_icon="👾", layout="wide")
st.title("Tic Tac Toe | You VS Computer")
st.write("Let's Start")
st.sidebar.success("Hy Everyone , This is my first project with Streamlit . Please play this simple game and have a good day ! \n\n Tashika")

if "board" not in st.session_state:
    st.session_state.board=["" for _ in range(9)]
    st.session_state.current_player="X"
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
    st.session_state.current_player="X"
    st.session_state.winner=None

def max_min(board,is_maximum):
    winner=check_winner(board)
    if winner=="O":
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
                best_score=min(score,best_score)
        return best_score
    

def ai_move():
    best_score=-float("inf")
    move = None
    for i in range(9):
            if st.session_state.board[i]=="":
                st.session_state.board[i]="O"
                score= max_min(st.session_state.board,False)
                st.session_state.board[i]=""
                if score > best_score:
                    best_score = score
                    move = i
    if move is not None:
           st.session_state.board[move]="O"         

def draw_board():
    for i in range(3):
        cols=st.columns(3)
        for j in range(3):
            idx = 3 * i + j
            if st.session_state.board[idx]=="":
                if cols[j].button(" ", key=idx):
                    if st.session_state.winner is None and st.session_state.current_player == "X":
                        st.session_state.board[idx] = "X"
                        st.session_state.winner = check_winner(st.session_state.board)
                        if st.session_state.winner is None:
                            ai_move()
                            st.session_state.winner = check_winner(st.session_state.board)
            else:
                cols[j].button(st.session_state.board[idx], key=idx, disabled=True)

draw_board()       



if st.session_state.winner:
    if st.session_state.winner == "Draw" :
        st.success("It's a draw 🤝 ")
    else:
        st.success(f"Player {st.session_state.winner} wins🏆")    
    st.button("Play again", on_click=reset_game)
elif st.session_state.current_player == "X" and st.session_state.winner is None:
    st.info("Your Turn (X). You'll go first.")

