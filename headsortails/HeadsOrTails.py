try:
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
		print("Better luck next time!")
		import sleepingdragons
except:
       import random
       def heads():
           return "heads"
       def tails():
           return "tails"
       ans = input("Heads or Tails?")
       if(random.choice([True,False])):
          coin_side = heads()
       else:
            coin_side = tails()
       if ans == coin_side:
	print("Correct!")
	OTHER_GAMES = input("Want to play a different game? This will be a screen based game ")
	if OTHER_GAMES == "Yes" or "yes":
		import sleepingdragons
       else:
	print("Wrong the correct answer was " + coin_side + " and not " + ans)
        print("Better luck next time")
	other_games = input("Want to play a different game? This will be a screen based game")  
	if other_games == "Yes" or "yes":
		import sleepingdragons
	else:
		print("Game Over!")	
