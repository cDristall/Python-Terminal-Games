# Import required modules
import os
import sys
import time
import shutil


def clear() -> None:
     os.system('cls' if os.name=='nt' else 'clear')
     return


def print_centre(s: str) -> None:
	print(s.center(shutil.get_terminal_size().columns))
	return


def input_centre() -> str:
	i = input(' '*((shutil.get_terminal_size().columns)//2-1))
	return i


# Define Global CONSTANTS 
WHITE = 1
BLACK = 2
# Used with WHITE & BLACK to print out the correct character
IDS = ' ●○'


class ConnectFour:
	"""Connect four checkers in a row to win!"""
	def __init__(self, height=6, width=7):
		self.width = width
		self.height = height
		self.board = [[0]*width for y in range(height)]
		self.turn = WHITE

	def draw_board(self) -> None:
		
		header = '╷' + '╷'.join('1234567') + '╷'
		print_centre(header)

		for row in self.board:
			sym = [IDS[value] for value in row]
			printable_row = '│' + '│'.join(sym) + '│'
			print_centre(printable_row)

		footer = '╰' + '─┴'*(self.width-1) + '─╯'
		print_centre(footer)
		return

	def check_for_wins(self) -> bool:

		key = [self.turn] * 4

		# Check for horizontal win
		for row in self.board:
			for i in range(self.width-3):
				if key == row[i:i+4]:
					return True

		# Check for vertical win | columns == a transposed self.board
		columns = [[row[i] for row in self.board] for i in range(self.width)]
		for col in columns:
			for j in range(self.height-3):
				if key == col[j:j+4]:
					return True

		# Check for Diagonal Wins
		for j in range(self.height-3):
			for i in range(self.width-3):
				a = [self.board[j][i], self.board[j+1][i+1],
					self.board[j+2][i+2], self.board[j+3][i+3]]
				if key == a:
					return True

		for j in range(self.height-1, 2, -1):
			for i in range(self.width-3):
				a = [self.board[j][i], self.board[j-1][i+1],
				     self.board[j-2][i+2], self.board[j-3][i+3]]
				if key == a:
					return True

		# No win condition found.  Returns False
		return False

	def get_user_move(self) -> int:
		
		print_centre(f"{IDS[self.turn]}'s turn, enter column or 'q' to quit:")
		
		while True:
			move = input_centre()

			if move == 'q':
				return move

			if move not in ['1', '2', '3', '4', '5', '6', '7']:
				print_centre("Enter a number from 1 to 7. Try again.")
				continue

			move = int(move) - 1

			# Check if chosen column is full
			if 0 not in [row[move] for row in self.board]:
				print_centre("Column is full. Enter another column.")
				continue
			else:
				# Return the move made
				return move

	def change_turn(self) -> None:
		"""Change who's turn it is from WHITE to Black & vice versa."""
		if self.turn == WHITE:
			self.turn = BLACK
		else:
			self.turn = WHITE
		return

	def update_board(self, move) -> None:
		"""Updates the board with user's inputed move."""
		for i in range(self.height-1, -1, -1):
			if self.board[i][move] == 0:
				self.board[i][move] = self.turn
				break
		return

	def no_moves_left(self) -> bool:
		"""Returns True or False if there are no spots left on the board."""
		flattened_board = [spot for row in self.board for spot in row]
		return (0 not in flattened_board)

	def run(self):
		"""Main game loop."""
		while True:

			# Pause, clear the terminal, & print out the current board
			time.sleep(0.4)
			clear()
			self.draw_board()

			# Check if the board is full
			if self.no_moves_left():
				print_centre("It's a draw.")
				break

			# Get the user to input a move
			# Then updates self.board or quit the loop & exit. 
			move = self.get_user_move()
			if move == 'q': break
			self.update_board(move)

			# Check for wins
			if self.check_for_wins():
				time.sleep(0.4)
				clear()
				self.draw_board()
				print_centre(f"Player-{IDS[self.turn]} has won!")
				break

			# Change who's turn it is
			self.change_turn()
		
		return


if __name__ == '__main__':
	game = ConnectFour()
	game.run()
	print_centre("Game Over. Press enter to exit.")
	# Used so program doesn't instantly exits the terminal.
	input_centre()
