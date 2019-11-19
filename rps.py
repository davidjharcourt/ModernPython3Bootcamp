import random
#from random import randrange

# Set up counter
player_wins = 0
computer_wins = 0
winning_score = 2

# for time in range(3):
while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins} Computer score: {computer_wins}")
	print(f"")
	print("...rock...")
	print("...paper...")
	print("...scissors!...")


	# Get player1 Input
	player = input("Player 1 enter choice: ").lower()
	if player == "quit":
		break

	# Get computer Input
	rand_num = random.randrange(3)
	computer = None
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"The computer plays {computer}")

	print("Shoot!")

	# Compare inputs based on rock-paper-scissor rules and print winner
	if player and computer:
		if player == computer:
			print("It's a tie! Play again")
		elif player == "rock":
			if computer == "paper":
				print("Paper covers rock! computer wins!")
				computer_wins += 1
			elif computer == "scissors":
				print("Rock breaks scissors! player wins!")
				player_wins += 1
		elif player == "paper":
			if computer == "rock":
				print("Paper covers rock! Player wins!")
				player_wins += 1
			elif computer == "scissors":
				print("Scissors cut paper! Computer wins!")
				computer_wins += 1
		elif player == "scissors":
			if computer == "rock":
				print("Rock breaks scissors! Computer wins!")
				computer_wins += 1
			elif computer == "paper":
				print("Scissors cut paper! Player wins!")
				player_wins += 1
		else:
			print("Something went horribly wrong!")

		if player_wins > computer_wins:
			print("You win!")
		else:
			print("You suck!")
