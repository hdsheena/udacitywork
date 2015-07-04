import random
again = 1
while again == 1:
	friendly = random.randint(1,2)
	print("You are in a land full of dragons. \nIn front of you, you see two caves. \nIn one cave, the dragon is friendly and will share his treasure with you. \nThe other dragon is greedy and hungry, and will eat you on sight.\n\n Which cave will you go into? (1 or 2)")
	guess = raw_input()
	guess = int(guess)
	print("You approach the cave...\nIt is dark and spooky...\nA large dragon jumps out in front of you! He opens his jaws and...")
	if guess == friendly:
		print("Invites you in.")
	else:
		print("Gobbles you down in one bite!")
	print("Do you want to play again? (yes or no)")
	play = raw_input()
	if play == 'yes':
		again = 1
	else:
		again = 0

