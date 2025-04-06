
import random 
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

global board
board = [[" " for x in range(3)] for y in range(3)]

def winner(b, l):
    return(
        (b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l) 
    )


def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == '':

        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner (board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match") 
    elif winner (board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match") 
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")


def isfree(i, j): 
    return board[i][j]

def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0): 
            flag = False
    return flag


def gameboard_pl(game_board, l1, l2): 
    global button 
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i) 
        button[i] = []
    for j in range(3):
        n = j
        button[i].append(j)
        get_t = partial (get_text, i, j, game_board, l1, l2) 
        button[i][j] = Button(
            game_board, bd=5, command=get_t, height=4, width=8) 
        button[i][j].grid(row=m, column=n)
    game_board.mainloop()


def pc():
    possiblemove = []
    for i in range(len (board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy (board) 
                boardcopy [i[0]][i[1]] = let 
                if winner (boardcopy, let): 
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]: 
                corner.append(i)
            if len(corner) > 0:
                move = random.randint(0, len (corner) - 1) 
                return corner [move]
            edge = []
            for i in possiblemove:
                if i in [[0, 1], [1, 0], [1, 2], [2, 1]]: 
                    edge.append(i)
            if len(edge) > 0:
                move = random.randint(0, len(edge) -1)
                return edge[move]