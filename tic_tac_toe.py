'''
Author: Cayden Ever
Sources: Mr. Campbell, Google for openai integration
Description: Allows user to play tic tac toe against random or against AI. 
Date: 4.2.2026
Bugs: when I put in a wrong answer the program breaks
'''
# Import random so the computer can make random moves and so we can randomly assign who goes first
import random
# Import time so we can pause for 1 second to make the computer feel like it's "thinking"
import time
# Import OpenAI so the computer can use AI to choose smart moves
from openai import OpenAI
# Create the OpenAI client (this uses the API key from your environment variables)
client = OpenAI()

# Tic-Tac-Toe
# This function prints the board in a clean format so the player can see the game state
def display_board(board):
    print()
    print("      Col 1 Col 2 Col 3")
    print("Row 1  " + board[0][0] + "  |  " + board[0][1] + "  |  " + board[0][2])
    print("      -----------------")
    print("Row 2  " + board[1][0] + "  |  " + board[1][1] + "  |  " + board[1][2])
    print("      -----------------")
    print("Row 3  " + board[2][0] + "  |  " + board[2][1] + "  |  " + board[2][2])
    print()

# This function converts the 2D board list into a string so the AI can read it more clearly
def board_to_string(board):
    """Converts the board list into a readable text format for the AI."""
    rows = []

    # Loop through each row of the board
    for row in board:
        # Replace empty spaces (' ') with underscores (_) so the AI can clearly see open spots
        rows.append(" ".join([cell if cell != ' ' else '_' for cell in row]))

    # Join all 3 rows into one multi-line string
    return "\n".join(rows)

# This function asks the OpenAI model to choose the best move for the computer
def get_ai_move(board, ai_shape):
    # Convert the board into a readable string first
    board_text = board_to_string(board)
    
    # This prompt gives the AI:
    # 1. The current board
    # 2. A coordinate map
    # 3. Its shape (x or o)
    # 4. Instructions to return ONLY row,col like 1,1
    # This helps reduce bad formatting and confusion
    prompt = f"""
You are a Tic-Tac-Toe Pro. 
Current Board:
{board_text}

Coordinate Map:
1,1 | 1,2 | 1,3
---------------
2,1 | 2,2 | 2,3
---------------
3,1 | 3,2 | 3,3

You are playing as {ai_shape}. 
Pick the best winning or blocking move.
Return ONLY row,col. Example: 1,1
"""
    try:
        # Send the prompt to the OpenAI model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # Get the model's answer as text (example: "2,3")
        move = response.choices[0].message.content.strip()

        # Print what the AI chose so you can see/debug it
        print(f"AI chose: {move}")
        
        # Standardize parsing:
        # Split the AI's response by comma, convert to int, and subtract 1
        # because user/AI thinks in 1-3 but Python lists use 0-2
        row = int(move.split(',')[0]) - 1
        col = int(move.split(',')[1]) - 1

        # Make sure the move is:
        # 1. Inside the board
        # 2. On an empty square
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = ai_shape
        else:
            # If AI gives a bad move, fall back to a random legal move
            get_random_move(board, ai_shape)

    except:
        # If anything goes wrong (bad format, API issue, etc.),
        # fall back to a random legal move so the game still works
        get_random_move(board, ai_shape)

# This function makes the computer choose a random open square
def get_random_move(board, shape):
    # Possible row/column indexes for a 3x3 board
    numbers = [0, 1, 2]

    # Keep trying random spots until an empty one is found
    while True:
        row = random.choice(numbers)
        col = random.choice(numbers)

        # Only place the shape if the spot is empty
        if board[row][col] == ' ':
            board[row][col] = shape
            break

# This function asks the human player for a move and validates the input
def get_player_move(board, shape):
    while True:
        try:
            # Ask for input like "1,1" and split into row and column
            player_move = input("Enter row and column (1-3) e.g. 1,1: ").split(",")
            
            # Use strip() in case the user types spaces like "1, 1"
            # Subtract 1 because user enters 1-3 but Python uses 0-2 indexes
            row = int(player_move[0].strip()) - 1
            col = int(player_move[1].strip()) - 1

            # Check that row and col are valid board positions
            if row in [0, 1, 2] and col in [0, 1, 2]:
                # Check that the chosen square is empty
                if board[row][col] == ' ':
                    board[row][col] = shape
                    break
                else:
                    print("That spot is taken. Try again.")
            else:
                print("Numbers must be between 1 and 3.")

        # Catch bad input such as letters, missing comma, missing number, etc.
        except (ValueError, IndexError):
            print("Invalid format. Please enter numbers only like 1,1")

# This function checks if anyone has won the game
def check_winner(board):
    "Return X,O, or none"

    # --- Check all winning possibilities for X ---

    # Rows
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        return 'x'
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        return 'x'
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        return 'x'

    # Columns
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        return 'x'
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        return 'x'
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        return 'x'

    # Diagonals
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        return 'x'
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        return 'x'

    # --- Check all winning possibilities for O ---

    # Rows - O
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        return 'o'
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        return 'o'
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        return 'o'

    # Columns - O
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        return 'o'
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        return 'o'
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        return 'o'

    # Diagonals - O
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        return 'o'
    elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        return 'o'

    # If no winner is found, return None
    else:
        return None

# This function checks if the board is full and nobody has won
def is_draw(board):
    "Return True if the board is full with no winner."

    # This goes through every cell in every row and checks that none are empty spaces
    # If every cell is NOT ' ', the board is full
    return all(cell != ' ' for row in board for cell in row) #iterates through the whole

# This is the main game function that controls the full Tic-Tac-Toe game
def play_game():
    # Create a fresh empty 3x3 board
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    # Ask the player which type of computer they want to play against
    # r = random mover
    # ai = OpenAI smart mover
    while True:
        game_choice = input("Would you like to play against random mover or ai (r/ai): ").lower()
        
        # Validate the game mode choice
        if game_choice not in ["r", "ai"]:
            print("Invalid choice. Please type either 'r' or 'ai'")
        else:
            break
    # Randomly assign whether the player goes first or second
    # 1 means player is X (goes first)
    # 2 means player is O (goes second)
    player_turn = random.randint(1, 2)

    if player_turn == 1:
        shape = 'x'      # Player is X
        ai_shape = 'o'   # Computer is O
    else:
        shape = 'o'      # Player is O
        ai_shape = 'x'   # Computer is X

    # Tell the player what shape they are
    print(f"You are playing as: {shape}")

    # Main game loop: keeps running until someone wins or it's a draw
    while True:
        # --- TURN LOGIC ---
        if shape == 'x':
            # Player goes first because X always starts

            # Get the player's move
            get_player_move(board, shape)

            # Show updated board
            display_board(board)

            # Check if player just won
            if check_winner(board) == 'x':
                print("x wins!")
                break

            # Check for draw
            elif is_draw(board):
                print("draw!")
                break

            # Computer turn
            print("Computer choosing...")
            time.sleep(1)

            # Choose AI move or random move depending on selected mode
            if game_choice == "ai":
                get_ai_move(board, ai_shape)
            else:
                get_random_move(board, ai_shape)
            
            # Show updated board
            display_board(board)

            # Check if computer just won
            if check_winner(board) == ai_shape:
                print(f"{ai_shape} wins!")
                break

            # Check for draw
            elif is_draw(board):
                print("draw!")
                break

        else:
            # Computer goes first because player is O

            # Computer turn first
            print("Computer choosing...")
            time.sleep(1)

            # Choose AI move or random move depending on selected mode
            if game_choice == "ai":
                get_ai_move(board, ai_shape)
            else:
                get_random_move(board, ai_shape)
                
            # Show updated board
            display_board(board)

            # Check if computer just won
            if check_winner(board) == ai_shape:
                print(f"{ai_shape} wins!")
                break

            # Check for draw
            elif is_draw(board):
                print("draw!")
                break

            # Player turn second
            get_player_move(board, shape)

            # Show updated board
            display_board(board)

            # Since player is O in this branch, check specifically for O win
            if check_winner(board) == 'o':
                print("o wins!")
                break

            # Check for draw
            elif is_draw(board):
                print("draw!")
                break

# This makes sure the game only starts when this file is run directly
# (not when imported into another Python file)
if __name__ == "__main__":
    play_game()