# Import required modules
import os
import sys
import time
import shutil

# Define Global CONSTANTS 
_X = 1
_O = 2
IDS = ' XO'
HEADER_MSG = [
	'      Tic-Tac-Toe                     ',
	'     -------------          0 | 1 | 2 ',
	'   Make your move by       ---+---+---',
	'  entering the number       3 | 4 | 5 ',
	'that corresponds to the    ---+---+---',
	'  square on the board.      6 | 7 | 8 ',
	'',
	'']


def clear() -> None:
     os.system('cls' if os.name=='nt' else 'clear')
     return

def print_centre(s: str) -> None:
	print(s.center(shutil.get_terminal_size().columns))
	return

def input_centre(s=' ') -> str:
	i = input(s*((shutil.get_terminal_size().columns)//2-1))
	return i

def print_header() -> None:
	for line in HEADER_MSG:
		print_centre(line)

class TicTacToe:
	"""A game of Tic-Tac-Toe. Get three in a row to win."""
	def __init__(self):
		self.board = [0 for i in range(9)]
		self.turn = _X

	def draw_board(self) -> None:
		"""Prints out the current game board."""
		line = "---+---+---"
		row_1 = f" {IDS[self.board[0]]} | {IDS[self.board[1]]} | {IDS[self.board[2]]} "
		row_2 = f" {IDS[self.board[3]]} | {IDS[self.board[4]]} | {IDS[self.board[5]]} "
		row_3 = f" {IDS[self.board[6]]} | {IDS[self.board[7]]} | {IDS[self.board[8]]} "
		print_centre(row_1)
		print_centre(line)
		print_centre(row_2)
		print_centre(line)
		print_centre(row_3)

	def check_for_wins(self) -> bool:
		"""Checks for any win conditions. Returns True if any found."""
		bd = self.board
		return ((bd[0] == bd[1] == bd[2] and bd[0] != 0) or
			   (bd[3] == bd[4] == bd[5] and bd[3] != 0) or
			   (bd[6] == bd[7] == bd[8] and bd[6] != 0) or
			   (bd[0] == bd[3] == bd[6] and bd[0] != 0) or
			   (bd[1] == bd[4] == bd[7] and bd[1] != 0) or
			   (bd[2] == bd[5] == bd[8] and bd[2] != 0) or
			   (bd[0] == bd[4] == bd[8] and bd[0] != 0) or
			   (bd[2] == bd[4] == bd[6] and bd[2] != 0))

	def get_user_move(self) -> int:
		"""Asks user to input a move and checks if it is a valid option."""
		
		print_centre(f"Player-{IDS[self.turn]} enter your move or 'q' to quit: ")
		
		while True:
			move = input_centre()

			if move == 'q': return move
				
			if move not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
				print_centre("Numbers 0 -  8 only. Try again.")
				continue

			move = int(move)
			if self.board[move] != 0:
				print_centre("That spot is already taken. Try again.")
				continue

			return move

	def change_turn(self) -> None:
		"""Change who's turn it is from _X to _O & vice versa."""
		if self.turn == _X:
			self.turn = _O
		else:
			self.turn = _X

	def run(self):
		"""Main game loop."""
		while True:
			
			# Pause, clear the terminal, & print out the current board.
			time.sleep(0.4)
			clear()
			print_header()
			self.draw_board()

			# Check if the board is full i.e. a draw
			if 0 not in self.board:
				print_centre("It's a draw.")
				break

			# Get the user to input a move
			# Then update self.board or quit the loop & exit.
			move = self.get_user_move()
			if move == 'q': break
			self.board[move] = self.turn

			if self.check_for_wins(): # Check for wins
				time.sleep(0.4)
				clear()
				print_header()
				self.draw_board()
				print_centre(f"Player-{self.turn} has won!")
				break

			self.change_turn() # Change who's turn it is
			# ========= End of loop =========



if __name__ == '__main__':
	game = TicTacToe()
	game.run()
	print_centre("Game Over. Press enter to exit.")
	# Used so program doesn't instantly exits the terminal.
	input_centre()
	clear()
	sys.exit()
