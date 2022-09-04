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
   other_games = input("want to play a different game? This game will be a screen-based game")
   if other_games == "Yes" or "yes":
       import sleepingdragons
else:
	 print("Wrong the correct answer was " + coin_side + " and not " + ans)
	 other_games = input("Want to play a different? This game will be a screen-based game")
	 if other_games == "Yes" or "yes":
	     import sleepingdragons
	 print("Better luck next time!")
