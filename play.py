###Globals###
board = ['-','-','-','-','-','-','-','-','-']
player=None
not_over=True
winner=None
run= None




def play():
    choose_player()
    display_()
    while not_over:
        check_input(player)
        check_game()
        flip()

    if winner =='X' or winner =='O':
        print(winner + " won.")

    elif winner == None:
        print("Tie.")
    play_again()
    

def choose_player():
    global player
    player = input("Choose Player 'X' / 'O'\n")

def play_again():
    print("Press o for play again---")
    print("Press x for finish---")
    run=input()
    if run=='o':
        play()
    elif run=='x':
        return 0

def display_():
    print(board[0] +' | '+ board[1] +' | ' +  board[2])
    print(board[3] +' | '+ board[4] +' | ' +  board[5])
    print(board[6] +' | '+ board[7] +' | ' +  board[8])

def check_game():
    check_win()
    check_tie()

    
def flip():
    global player
    if player=='X':
        player='O'
    elif player=='O':
        player='X'
    return


    
def check_input(player):
    position=input("Player "+player+", Choose a position from 1-9: ")
    while position not in ['1','2','3','4','5','6','7','8','9'] or board[int(position)-1] !='-':
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print("Invalid Input")
            position=input("Player "+player+" Choose a position from 1-9: ")
        elif board[int(position)-1]!='-':
            print("Position already taken.",end ="")
            position=input("Player "+player+" Choose an available position from 1-9: ")
        
    pos=int(position)-1
    board[pos]= player
    display_()



def check_win():

    global winner
    row_winner=check_win_row()
    column_winner=check_win_column()
    diagonal_winner=check_win_diagonal()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_tie():
    global not_over
    if '-' not in board:
        not_over=False
    return


def check_win_row():
    global not_over
    row1 = board[0]==board[1]==board[2]!='-'
    row2 = board[3]==board[4]==board[5]!='-'
    row3 = board[5]==board[6]==board[7]!='-'

    if row1 or row2 or row3:
        not_over=False
        if row1:
            return board[0]
        elif row2:
            return board[3]
        elif row3:
            return board[6]
    return

def check_win_column():
    global not_over
    col1 = board[0]==board[3]==board[6]!='-'
    col2 = board[1]==board[4]==board[7]!='-'
    col3 = board[3]==board[5]==board[8]!='-'

    if col1 or col2 or col3:
        not_over=False
        if col1:
            return board[0]
        elif col2:
            return board[1]
        elif col3:
            return board[2]
    return

def check_win_diagonal():
    global not_over

    if board[0]==board[4]==board[8] !='-':
        not_over=False
        return board[4]
    elif board[6]==board[4]==board[2] !='-':
        not_over=False
        return board[4]
    return

play()
