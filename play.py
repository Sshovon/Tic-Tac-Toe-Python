
###Globals###
board = ['-','-','-','-','-','-','-','-','-']
player="none"
not_over=True
winner="none"





def play():
    player = input("Choose Player 'X' / 'O'\n")
    display_()
    while not_over:
        check_input(player)
        check_game()
        flip()





def display_():
    print(board[0] +' | '+ board[1] +' | ' +  board[2])
    print(board[3] +' | '+ board[4] +' | ' +  board[5])
    print(board[6] +' | '+ board[7] +' | ' +  board[8])

def check_game():
    check_win()
    check_tie()

    
def flip():
    return


    
def check_input(player):
    position=input("Choose a position from 1-9: ")

    pos=int(position)-1

    board[pos]='X'
    display_()
def check_win():
    #check_win_row()
    #check_win_column()
    #check_win_diagonal()

    return

def check_tie():
    return

play()
