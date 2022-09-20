#!/usr/bin/ipython3

import random

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = {rock: scissors, paper: rock, scissors: paper }

playerScore = 0
computerScore = 0

def start():
	print("Let's play a game of Rock, Paper, Scissors")
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1, 3)
	result(player, computer)
	return playAgain()

def move():
	while True:
		print("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			player = int(input())
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print("Ooops! i didn't understand that. Please enter 1, 2, or 3")

def result(player, computer):
	print("Player threw {}\n".format( names[player] ) )
	print("Computer threw {}".format (names[computer]) )
	global playerScore, computerScore
	if player == computer:
		print("\nTie\n")
	else:
		if rules[player] == computer:
			print("\nPlayer win!\n")
			playerScore +=1
		else:
			print("\nComputer win\n")
			computerScore +=1

def playAgain():
	answer = input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", 'yes', 'Yes'):
		return answer
	else:
		print("Thanks you very much for playing out game. See you next time!")

def scores():
	global playerScore, computerScore
	print("High Scores")
	print("Player: ", playerScore)
	print("Computer: ", computerScore)

if __name__ == '__main__':
	start()











