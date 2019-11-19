print("...rock...")
print("...paper...")
print("...scissors!...")

# Get Player1 Input
Player1 = input("Player 1 enter choice: ")
print("***NO CHEATING\n\n" * 20)
# Get Player2 Input
Player2 = input("Player 2 enter choice: ")
print("Shoot!")

# Compare inputs based on rock-paper-scissor rules and print winner
if Player1 and Player2:
	if Player1 == Player2:
		print("It's a tie! Play again")
	elif Player1 == "rock":
		if Player2 == "paper":
			print("Paper covers rock! Player2 wins!")
		elif Player2 == "scissors":
			print("Rock breaks scissors! Player1 wins!")
	elif Player1 == "paper":
		if Player2 == "rock":
			print("Paper covers rock! Player1 wins!")
		elif Player2 == "scissors":
			print("Scissors cut paper! Player 2 wins!")
	elif Player1 == "scissors":
		if Player2 == "rock":
			print("Rock breaks scissors! Player2 wins!")
		elif Player2 == "paper":
			print("Scissors cut paper! Player 1 wins!")
	else:
		print("Something went horribly wrong!")

