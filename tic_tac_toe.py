# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


# Function for... (choosing a player?)
#def blablabla():
 #   pass


# ... write as many functions as you need


# Tic-tac-toe game
#if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
 #   print("Welcome to a new round of Tic-Tac-Toe!")

board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
player1 = input("Player 1 (x): ")
player2 = input("Player 2 (o): ")
current_player = player1
current_marker = "x"                
numdraw = 0

while True:
# start loop here 
    print(f"{current_player} it's your turn.")
    draw = input("Please enter your desired coordinates: ")                                 #change to int later!
    row = int(draw[0])
    col = int(draw[1])
    if board[row][col] == ' ':
        board[row][col] = current_marker  
    else: 
        print("This position is taken. Choose another position.")
        continue                                                                        #continue to jump up

    print_board(board)

#winning conditions
    if board[0].count(current_marker)==3 or board[1].count(current_marker)==3 or board[2].count(current_marker)==3:
        print("We have a winner!", current_player)
        break

    if board[0][0] == current_marker and board[1][1] == current_marker and board[2][2] == current_marker:
        print("We have a winner!", current_player)
        break

    if board[0][2] == current_marker and board[1][1] == current_marker and board[2][0] == current_marker:
        print("We have a winner!", current_player)
        break

    positions = []
    for n in board:
        for idx,element in enumerate(n):
            if element == current_marker:
                positions.append(idx)

    if positions.count(0)==3 or positions.count(1)==3 or positions.count(2)==3:
        print("We have a winner!", current_player)
        break

#draw condition
    numdraw += 1
    if numdraw == 9:                
        print("We have a draw!")
        break

#change player 
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

#change marker
    if current_marker == "x":
        current_marker = "o"
    else:
        current_marker = "x"