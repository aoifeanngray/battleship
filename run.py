# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

hidden_board = [[''] * 8 for x in range(8)]
guess_board = [[''] * 8 for x in range(8)]

letters_to_numbers = {'a': 0, 'b': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

# to see the board.
def print_board(board):
    print(' a,b,c,d,e,f,g,h')
    print(' --------')
    row_number= 1
    for row in board:


# create ships.
def create_ships():
    pass

# ask user what row and column they want to guess.
def get_ship_location():
    pass

# count the ships hit.
def count_hit_ships():
    pass
