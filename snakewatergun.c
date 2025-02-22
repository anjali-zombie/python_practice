resume = 'y'
while( resume != 'n'):
	player1 = input("player1 enter your guess:")
	player2 = input("player2 enter your guess:")

	if (player1 == "snake" and player2 == "water"):
		print("yayyyyyyyyyyyyyy!!!!player1 wins!!!!!!!!!!!!!!!!!")

	elif (player1 == "water" and player2 == "snake"):
		print("yayyy!!!!!!!!!!!!player2 wins!!!!!!!!!!!!!!")

	elif (player1 == "snake" and player2 == "gun"):
		print("yayyyyyyy!!!!!!player2 wins!!!!!!!!!!!!!!")

	elif (player1 == "gun" and player2 == "snake"):
		print("yayyyy!!!!!!!!!player1 wins!!!!!!!!!!!!!!")

	elif (player1 == "water" and player2 == "gun"):
		print("yayyyy!!!!!!!!player2 wins!!!!!!!!!!!!!!!!!!!!!!!!!")

	elif (player1 == "gun" and player2 == "water"):
		print("yayyyyyyyy!!!!!!!!player1 wins!!!!!!!!!!!!!!!!!!!!!")
	
	elif (player1 == "gun" and player2 == "water"):
		print("ohhhh!!!!!! its a draw")

	elif (player1 == "gun" and player2 == "water"):
		print("ohhhhhh!!!!! its a draw")

	elif (player1 == "gun" and player2 == "water"):
		print("ohhhhhh !!!!!! its a draw")
	else:
	 	print("enter valid guess")


	resume = input("enter if you want to continue this game or not[y/n]:")	




