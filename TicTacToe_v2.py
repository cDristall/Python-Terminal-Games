# Import required modules
import os
import sys
import time
import shutil

# Define Global Constants
_X = 1
_O = 2
ID = ' XO'
PAUSE_TIME = 0.4

HEADER_MSG = [ # Banner for display at top of screen.
	'╭─────────────────────────╥───────────────╮',
	'│       TIC TAC TOE       ║   7 │ 8 │ 9   │',
	'│      *************      ║  ───┼───┼───  │',
	'│  Select a space on the  ║   4 │ 5 │ 6   │',
	'│  board by entering its  ║  ───┼───┼───  │',
	'│  corresponding number.  ║   1 │ 2 │ 3   │',
	'╰─────────────────────────╨───────────────╯',
	' ']

INPUT_TO_INDEX = { # Translate user input to board index
    '7': 0, '8': 1, '9': 2,
    '4': 3, '5': 4, '6': 5,
    '1': 6, '2': 7, '3': 8}


def clear() -> None:
	"""Clear the terminal of all text."""
	os.system('cls' if os.name=='nt' else 'clear')
	return

def print_centre(s: str) -> None:
	"""Prints a string formated to the center of the terminal."""
	print(s.center(shutil.get_terminal_size().columns))
	return

def input_centre(s=' ') -> str:
	"""Centers user's input so it is aligned with rest of the text."""
	i = input(s*((shutil.get_terminal_size().columns)//2-1))
	return i

def print_header() -> None:
	"""Loops and prints the banner centered to the terminal."""
	for line in HEADER_MSG:
		print_centre(line)


class TicTacToe:
	"""A game of Tic-Tac-Toe. Get three in a row to win."""
	def __init__(self):
		"""Create a list full of 0's and sets the turn to Player-x."""
		self.board = [0 for i in range(9)]
		self.turn = _X

	def draw_board(self) -> None:
		"""Prints out the current game board."""
		bd = [ID[spot] for spot in self.board]
		print_centre(f" {bd[0]} │ {bd[1]} │ {bd[2]} ")
		print_centre("───┼───┼───")
		print_centre(f" {bd[3]} │ {bd[4]} │ {bd[5]} ")
		print_centre("───┼───┼───")
		print_centre(f" {bd[6]} │ {bd[7]} │ {bd[8]} ")
		print_centre(" ")

	def check_for_wins(self) -> bool:
		"""Checks for any win conditions. Returns True if any found."""
		bd = self.board # copy the gameboard for readability
		return ((bd[0] == bd[1] == bd[2] and bd[0] != 0) or
			    (bd[3] == bd[4] == bd[5] and bd[3] != 0) or
			    (bd[6] == bd[7] == bd[8] and bd[6] != 0) or
			    (bd[0] == bd[3] == bd[6] and bd[0] != 0) or
			    (bd[1] == bd[4] == bd[7] and bd[1] != 0) or
			    (bd[2] == bd[5] == bd[8] and bd[2] != 0) or
			    (bd[0] == bd[4] == bd[8] and bd[0] != 0) or
			    (bd[2] == bd[4] == bd[6] and bd[2] != 0))

	def get_user_move(self) -> int:
		"""Ask user to input a move & checks if it is a valid option."""
		print_centre(f"Player-{ID[self.turn]} enter your move or 'q' to quit.")
		while True:

			move = input_centre()
			
			if move == 'q' or move == 'quit': return 'q'

			if move not in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
				print_centre("Numbers 1 - 9 only. Try again.")
				continue

			if self.board[INPUT_TO_INDEX[move]] != 0:
				print_centre("That spot is already taken. Try again.")
				continue

			return INPUT_TO_INDEX[move]

	def change_turn(self) -> None:
		"""Change who's turn it is from _X to _O & vice versa."""
		if self.turn == _X:
			self.turn = _O
		else:
			self.turn = _X

	def run(self):
		"""Main Game Loop."""
		while True:

			# Pause, clear the terminal, & print out the current board.
			time.sleep(PAUSE_TIME)
			clear()
			print_header()
			self.draw_board()

			# Check if the board is full i.e. a draw
			if 0 not in self.board:
				print_centre("It's a draw.")
				break

			# Get the user's input & update the board
			# or quit the lop & exit game.
			move = self.get_user_move()
			if move == 'q': break
			self.board[move] = self.turn

			# Check for wins
			if self.check_for_wins():
				time.sleep(PAUSE_TIME)
				clear()
				print_header()
				self.draw_board()
				print_centre(f"Player-{ID[self.turn]} has won!")
				break

			# Change who's turn it is
			self.change_turn()
			# ========= End of loop =========


if __name__ == '__main__':
	game = TicTacToe()
	game.run()
	print_centre("Game Over. Press enter to exit.")
	# Used so program doesn't instantly exit the terminal.
	input_centre()
	clear()
	sys.exit()