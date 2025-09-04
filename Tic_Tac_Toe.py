import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    global winner
     # All possible winning combinations (rows, columns, diagonals)
    for combo in [[0,1,2],[3,4,5],[6,7,8],[2,4,6],[1,4,7],[0,4,8],[0,3,6],[2,5,8]]:
         # Check if all 3 buttons in the combo have the same text (X or O)
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
             # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show popup with winner info
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return True   # A winner is found
    return False  # no winner yet

# Function to check if the game is tied
def check_tie():
     # Tie happens when all buttons are filled and no winner yet
    if all(button["text"] != "" for button in buttons) and not winner:
        # Make all buttons orange if it's a tie
        for btn in buttons:   # 🔹 make all blocks orange
            btn.config(bg="orange")
         # Show popup for tie
        messagebox.showinfo("Tic-Tac-Toe", "Match Tied!")
        return True
    return False

# Function for button click (when player makes a move)
def button_click(index):
    global winner
    # Only allow move if button is empty and game is not over
    if buttons[index]["text"] == "" and not winner:
        # Place the current player's symbol (X or O)
        buttons[index]["text"] = current_player
        if check_winner():  # ✅ check win first
            winner = True
            return
        if check_tie():  # ✅ check tie after win check
            return
        toggle_player()

# Function to toggle between players
def toggle_player():
    global current_player
    if not winner: # Only switch if no winner
        # Change player from X → O or O → X
        current_player = "X" if current_player == "O" else "O"
        # Update label text to show current player’s turn
        label.config(text=f"Player {current_player}'s turn")


# ---------------- MAIN PROGRAM ---------------- #

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create 9 buttons for the 3x3 board
buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    for i in range(9)
]

# Place buttons in grid (3x3 layout)
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i % 3)

# Initialize first player and winner flag
current_player = "X"
winner = False

# Label to show current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)


# Start the Tkinter event loop
root.mainloop()
