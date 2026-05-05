'''
Author: Cayden Ever
Sources: Mr. Campbell, Google for special characters
Description: Allows user to play battleship against computer
Date: 5.5.2026
Bugs: n
'''
import time
import random

#declaring special characters as variables for usage in the battleship board
EMPTY = '~'         
SHIP  = 'X'
HIT   = '💥'
MISS  = '•'

def display_board(player_board):
    '''
    Displays the board in a user friendly way
    Args:
        player_board - for each cell if variables print a special character in its place
    '''
    print("\n    1    2    3    4    5")
    print("  " + "─" * 29)
    for i, row in enumerate(player_board): # for each row in board
        display_row = [] #set dislay_row as empty
        for cell in row: # for each cell in a  row
            if cell == EMPTY: # if cell is empty
                display_row.append('🌊') #add the water emoji in its place
            elif cell == HIT:   #if the cell is hit
                display_row.append('💥')  #put a explosion emoji in its place
            elif cell == MISS: #if cell is a miss from users shot
                display_row.append('•  ') #put a dot in its place
            elif cell == SHIP: # ADD THIS - if cell has a ship
                display_row.append('🚢') # Show ship emoji (or use '⛴️' or 'X  ')
            else:
                display_row.append('?  ') #anything else put a question mark
        print(f"{i+1} │ " + "  ".join(display_row)) #join all cells to be one board
        if i < len(player_board) - 1: #if the index is smaller than the length of the board (if still more cells need to be iterated through)
            print("  " + "─" * 29) #print the cell with its boundrie round it
    print()
def get_player_move(board, player_board):
    '''
    asks the player for their move and displays messages to user and tells them if they hit or miss the robots ships.
    Args:
        board - the board for the robot where the actual ships are stored
        player_board - the board the user sees that tracks if they hit or miss robot placed ships
    '''
    while True:
        try:
            player_move = input("Enter row and column to shoot at computer ships (1-5) e.g. 1,1: ").split(",") #ask user for rows and collumns for their shot
            row = int(player_move[0].strip()) - 1 #strip any extra characters the user puts in 
            col = int(player_move[1].strip()) - 1 #same for collumn

            if row in [0, 1, 2, 3, 4] and col in [0, 1, 2, 3, 4]: #if the users selection is with in range
                if board[row][col] == EMPTY: #if the cell at the users choice is empty
                    print("\n🚀 Firing missile") #displaying fire missle
                    #print 3 dots in a computer like way
                    for _ in range(3): #for 3 times
                        time.sleep(0.5)  #stop program for half second
                        print(".")      #print a period
                    time.sleep(0.5) #wait half a second
                    print("\n\n MISS...\n") #print miss to the user
                    board[row][col] = MISS #set board to miss at the cell
                    player_board[row][col] = MISS #set the player board to miss sa well
                    return
                elif board[row][col] == SHIP: #if the users shot is on the cell of a ship
                    print("\n🚀 Firing missile") #print fire message to the user
                    for _ in range(3): #loop 3 times
                        time.sleep(0.5) #wait half a second
                        print(".")      #print a period
                    time.sleep(0.5)     #wait half asecond
                    print("\n\n💥 DIRECT HIT!\n") #print a hit message to the user
                    board[row][col] = HIT #set the board to be displayed at index to hit
                    player_board[row][col] = HIT #set the player board to a hit
                    return
                else:
                    print("That spot is taken. Try again.")  #if the spot is taken print an error statment
            else:
                print("Numbers must be between 1 and 5.") #if the spot is outside range print error statment
        except (ValueError, IndexError): #If there is a seperate value error like special characters
            print("Invalid format. Please enter numbers only like 1,1") #print an invalid format statment

def get_player_ships(player_ship_board):
    '''
    Asks the user to either manually select ships or randomly select their ships
    Args: 
        player_ship_board - stores the player ship choices and the computer's shot selection
    Returns:
        the player_ship_board with the user's moves on it
    '''
    turns = 1  #set the turns to 1
    while True:
        manual_computer = input("Its time to select your ships! Would you like to manually select or choose random locations? type m for manual and r for random: ").lower() #ask user for either manual or random selection and convert it to lowercase
        
        if manual_computer == "m":  #if the user chooses manual
            while turns < 6:  #set the amount of turns they have to 5
                try:
                    player_ship = input(f"Enter row and column for your ship #{turns} selection (1-5) e.g. 1,1: ").split(",") #ask the user for their coordinates to fire at the compute ships
                    row = int(player_ship[0].strip()) - 1  #subtract one from row to match the index of python starting at zero
                    col = int(player_ship[1].strip()) - 1  #subtract one from collumn to match the index of python starting at zero
                    
                    if row in [0, 1, 2, 3, 4] and col in [0, 1, 2, 3, 4]: #if the choices are within the range of the coordinates of the board
                        if player_ship_board[row][col] == SHIP: #if there is a ship at the index already
                            print("You already placed a ship there! Try again.") #print there already is a ship there
                        else:
                            player_ship_board[row][col] = SHIP #if the spot is free set the location to a ship
                            turns += 1 #take up one turn
                    else:
                        print("Your selections must be between 1-5.") #if its out of range print error statment
                        
                except (ValueError, IndexError):
                    print("Enter selections in this format: 1,2") #if there is a value or index error print error statment
            
            print("Here are all of your board choices:") #print message to users.
            time.sleep(2) #wait two seconds
            display_board(player_ship_board) #show the player moves
            return player_ship_board #return the board with the player's ships placed
            
        elif manual_computer == "r": #if the user chooses random selection
            player_ship_coords = set() #track the coordinates
            
            while len(player_ship_coords) < 5: #while there are 5 coordinates left to place
                row = random.randint(0, 4) #set the row to a random coordinate 1-5
                col = random.randint(0, 4) #set the collumn to a random coordinate 1-5
                
                if (row, col) not in player_ship_coords: #if the coordinates are not in the list of tracked coordinates
                    player_ship_coords.add((row, col)) #add the coordinate to the list of picked coordinates
                    player_ship_board[row][col] = SHIP #set the player's board to have a ship at the coordinates
            
            print("Random ships placed!") #print success message
            time.sleep(2) #wait 2 seconds
            display_board(player_ship_board) #show the board
            return player_ship_board #return the board with the player's ships placed
        else:
            print("valid format.type either 'm' or 'r'") #print error message if not a valid format

def play_game():
    board        = [[EMPTY for _ in range(5)] for _ in range(5)]  #create a 5 by 5 board for computer ships
    player_board = [[EMPTY for _ in range(5)] for _ in range(5)]  #create a 5 by 5 board for player display
    player_ship_board = [[EMPTY for _ in range(5)] for _ in range(5)] #create a 5 by 5 board for player's ships

    # Computer random ship choice
    ship_coords = [] #create an empty list to track ship coordinates
    while len(ship_coords) < 5: #loop 5 times
        row = random.randint(0, 4) #pick a random row between 1,5
        col = random.randint(0, 4) #pick a random collumn between 1,5
        if (row, col) not in ship_coords: #if the random coords are not already choosen
            ship_coords.append((row, col)) #add them to the list of chosen coordinates
            board[row][col] = SHIP #set the board to have a ship at the chosen coords
    
    turns = 10  #set player turns to 10
    print("Welcome to Battleship!")  #welcome message
    print("Sink all 5 ships in 10 turns to win!\n") #instructions
    get_player_ships(player_ship_board)
    computer_shots = set()  # Track computer's previous shots

    while turns > 0:  #while user still has turns left
        time.sleep(1)  #wait 1 second
        display_board(player_board)  #show the player the board
        get_player_move(board, player_board) #get the player's move
        turns -= 1 #subtract 1 turn

        hits = sum(cell == HIT for row in board for cell in row) #set hits equal to every cell that = hit on the board

        if hits == 5: #if player hits all 5 of the computer's ships
            display_board(player_board)  #display the board
            print(f" You sank all 5 ships in {10 - turns} turns! YOU WIN!\n") #print win message
            return
        
        # Computer's turn - loop until finding an untargeted cell
        while True:
            row = random.randint(0, 4)   #pick a random row between 1-5
            col = random.randint(0, 4)   #pick a random col between 1,5
            
            if (row, col) not in computer_shots:  # Check if not already shot
                computer_shots.add((row, col))  # Mark the row and collumn the computer chooses as shot
                
                if player_ship_board[row][col] == EMPTY: #if the player's board is empty at the coords
                    print("\n🚀 Computer Firing missile")   #print firing message
                    #loading animation
                    for _ in range(3):   #3 times loop
                        time.sleep(0.5) #wait half a second
                        print(".")      #print a period
                    time.sleep(0.5)     #wait another half a second
                    print("\n\n Computer MISS...\n") #print miss message
                    time.sleep(2)    #wait 2 seconds
                    player_ship_board[row][col] = MISS  #set the player board to a miss by the computer
                    break
                    
                elif player_ship_board[row][col] == SHIP:  #if the computer picks the coords of a player ship
                    print("\n🚀 Computer Firing missile")   #print firing message
                    #loading animation
                    for _ in range(3): #loop 3 times
                        time.sleep(0.5)  #wait half a second
                        print(".")  #print a period
                    time.sleep(0.5)  #wait half a second
                    print("\n\n💥 Computer DIRECT HIT!\n")  #print direct hit message
                    time.sleep(2)   #wait 2 seconds
                    player_ship_board[row][col] = HIT  #set the player board to hit at the coords
                    break
    #once turns run out
    display_board(player_board)  #show the player the board
    hits = sum(cell == HIT for row in board for cell in row) #calculate total hits
    print(f"Out of turns! You sank {hits}/5 ships. Game over.\n") #print game over message
if __name__ == "__main__":
    play_game()