import random
def heads():
	return "heads"
def tails():
	return "tails"
ans = input("Heads or Tails? \n")
if random.choice([True, False]):
   coin_side = tails()
else:
	 coin_side = heads()
if ans < coin_side:
   print("Correct \n")
   print("Game won!")
else:
	 print("Wrong the correct answer was " + coin_side + " and not " + ans + "." "\n")
	 print("Better luck next time!")
