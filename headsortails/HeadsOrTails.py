import random
def heads():
	return "heads"
def tails():
	return "tails"
ans = input("Heads or Tails? ")
if random.choice([True, False]):
   coin_side = tails() 
else:
	 coin_side = heads()
if ans == coin_side:
   print("Correct!")
else:
	print("Wrong the correct answer was " + coin_side + " and not " + ans)
	play_new_game = input("Want to play a new game?")
	if play_new_game == "yes":
		print("Loading new game")
		def Correct_answer():
		    return "Correct Answer!"
		def Wrong_answer():
		    return "Wrong answer!"
	        question = input("What's 5+5")
		if question == 10:
			Correct_answer()
		else:
			Wrong_answer()
	else:
		print("Game Over")
