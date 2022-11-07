# Import required modules
import os
import sys
import time


# Define Global Variables 
WHITE = 1
BLACK = 2
# IDS[0] = ' ' | IDS[1] = '●' | IDS[2] = '○'
IDS = ' ●○'


def clear() -> None:
     os.system('cls' if os.name=='nt' else 'clear')
     return None


class ConnectFour:
	"""
	Connect four checkers in a row to win!
	"""
	def __init__(self, height=6, width=7):
		self.width = width
		self.height = height
		self.board = [[0]*width for y in range(height)]
		self.turn = WHITE


	def draw_board(self) -> None:
		
		header = '\t\t  ╷' + '╷'.join('1234567') + '╷'
		print(header)

		for row in self.board:
			sym = [IDS[value] for value in row]
			printable_row = '\t\t  │' + '│'.join(sym) + '│'
			print(printable_row)

		footer = '\t\t  ╰' + '─┴'*(self.width-1) + '─╯'
		print(footer)


	def check_for_wins(self) -> bool:

		key = [self.turn] * 4

		# Check for horizontal win
		for row in self.board:
			for i in range(self.width-3):
				if key == row[i:i+4]:
					return True

		# Check for vertical win
		columns = [[row[i] for row in self.board] for i in range(self.width)]
		for col in columns:
			for j in range(self.height-3):
				if key == col[j:j+4]:
					return True


		# Check for Diagonal Wins
		for j in range(self.height-3):
			for i in range(self.width-3):
				a = [self.board[j][i], self.board[j+1][i+1], self.board[j+2][i+2], self.board[j+3][i+3]]
				if key == a:
					return True

		for j in range(self.height-1, 2, -1):
			for i in range(self.width-3):
				a = [self.board[j][i], self.board[j-1][i+1], self.board[j-2][i+2], self.board[j-3][i+3]]
				if key == a:
					return True

		# No win condition found.  Returns False
		return False


	def get_user_move(self) -> int:
		
		print(f"\t{IDS[self.turn]}'s turn, enter column or 'q' to quit:")
		
		while True:
			move = input('\t\t\t ')

			if move == 'q':
				print("\t   Game Over. Press enter to exit.")
				input('\t\t\t ')
				sys.exit()

			if move not in ['1', '2', '3', '4', '5', '6', '7']:
				print(" Input not recognized.  Enter a single number from 1 to 7.")
				continue

			try:
				move = int(move) - 1
			except:
				print("\tInput not recognized. Try again.")
				continue

			col = [row[move] for row in self.board]
			if 0 not in col:
				print("\t Column is full. Enter another column.")
				continue

			else:
				return move


	def change_turn(self) -> None:
		if self.turn == WHITE:
			self.turn = BLACK
		else:
			self.turn = WHITE
		return


	def update_board(self, move) -> None:
		for i in range(self.height-1, -1, -1):
			if self.board[i][move] == 0:
				self.board[i][move] = self.turn
				break
		return


	def run(self):

		move_count = 0

		while True:

			time.sleep(0.5)
			clear()

			# Print out the current board
			self.draw_board()

			# Check if the max number of moves have been made
			if move_count >= (self.height * self.width):
				print("\t\tIt's a draw.")
				break

			# Get the user to input a move.
			move = self.get_user_move()

			# Update the board
			self.update_board(move)

			# Check for wins
			# TODO: Check for vertical wins
			if self.check_for_wins():
				time.sleep(0.5)
				clear()
				self.draw_board()
				print(f"\t\t  Player-{IDS[self.turn]} has won!")
				break

			# Change who's turn it is
			self.change_turn()

			# Update the move count
			move_count += 1

		return





if __name__ == '__main__':
	game = ConnectFour()
	game.run()
	print("\t   Game Over. Press enter to exit.")
	input('\t\t\t ')
