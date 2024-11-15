# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
#board=[["1","2","3"],["4","5","6"],["7","8","9"]]

def print_board(board):
   
    print(board[0])
    print(board[1])
    print(board[2])

def board_update(pos, board, marker):
    board[(int(pos)-1)//3][board[(int(pos)-1)//3].index(pos)]=marker
    return board



# Tic-tac-toe game
#if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
 #   print("Welcome to a new round of Tic-Tac-Toe!")

board=[["1","2","3"],["4","5","6"],["7","8","9"]]
position_list=list("123456789")

winning_sets=["123","456","789","147","258","369","159","357"] 

print("Welcome to a new round of Tic-Tac-Toe!")
print("you can choose one of the positions 1-9 while making move")
print_board(board)

player1=input("Player1 Enter Your Name:")
player2=input("Player2 Enter Your Name:")
players={player1:[],player2:[]}

player=player1
marker="X"

winner_found=0
draw_num=0

while True:
    position_input=input(f"{player} choose your free position: ")

    if position_input not in players[player1]+players[player2] and position_input in position_list:
        players[player].append(position_input)
    else:
        print("this position is wrong, please choose another one")
        continue

    board=board_update(position_input,board,marker)
    print_board(board)

    draw_num +=1
    if draw_num>= 5:
        for win in winning_sets:
            if set(players[player]).intersection(set(list(win))) == set(list(win)):
                print("We have a winner: ", player)
                winner_found=1
                break
        if winner_found: break    
#players[player].intersection(winning_set)==winning_set
        if draw_num==9:
            print("We have a draw!")
            break

    player=[player2,player1][int(draw_num % 2 == 0)]
    marker=["O","X"][int(draw_num % 2 == 0)]