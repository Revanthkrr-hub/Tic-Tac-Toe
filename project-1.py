
# coding: utf-8

# In[ ]:


from __future__ import print_function


# In[ ]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('  |  |  ')
    print('' + board[7] + ' | ' + board[8] +  '| ' +  board[9])
    print('  |  |  ')
    print('----------')
    print('  |  |  ')
    print('' + board[4] + ' | '+ board[5] + '| '+  board[6])
    print('  |  |  ')
    print('----------')
    print('  |  |  ')
    print('' + board[1] + ' | ' + board[2] + '| '+ board[3])
    print('  |  |  ')
    


# In[ ]:


def player_input():
    
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input("do u want x or o").upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


# In[ ]:


def place_marker(board,marker,position):
    board[position] = marker


# In[ ]:


def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[2]==mark and board[5]==mark and board[8]==mark) or
            (board[3]==mark and board[6]==mark and board[9]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[3]==mark and board[5]==mark and board[7]==mark))


# In[ ]:


import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'


# In[ ]:


def space_check(board,position):
    return board[position] == ' '


# In[ ]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[ ]:


def  player_choice(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position =raw_input('enter the position u want to choose from (1,9)')
    return int(position)


# In[ ]:


def replay():
    return raw_input('do you want to  play again yes or no').lower().startswith('y')


# In[ ]:


print("wlcm to the tic tac toe game..!!!")
while True:
    theboard=[' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + 'choice to play')
    game_on = True
    
    while game_on:
        if turn == 'player1':
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard,player1_marker,position)
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print("player1 won")
                game_on= False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("game is draw")
                    break
                else:
                    turn = 'player2'
        else:
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard,player2_marker,position)
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print("player2 won")
                game_on= False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("game is draw")
                    break
                else:
                    turn= 'player1'
    if not replay():
            break

