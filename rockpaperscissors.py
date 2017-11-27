import random # Import the 'random' module, so we can use it to generate a random number

        
def game():
    stuff = ["rock", "paper", "scissors"] #Assign rock, paper or scissors to 'stuff'
    computer = stuff[random.randint(0,2)] #Array starts at 0, randint pick a random number from 0 to 2, each number is related to the string. (0 = Rock, 1 = Paper, 2 = Scissors)
    user = input("Rock, Paper or Scissors.\n")
    user = user.lower() # Make users input lowercase


    if user == computer: # Check if user & computer picked the same thing
        print ("You both picked", user)
        game() #Loop so the game plays again
        
    elif user == "rock": # Logic to decide if you or the computer win
         if computer == "scissors":
             print ("You win rock beats scissors.\n")
             game() #Loop so the game plays again
         else:
            print ("You lose" + " " + computer + " " + "beats" + " " + user)
            game() #Loop so the game plays again

    elif user == "paper": # Logic to decide if you or the computer win
        if computer == "rock":
           print ("You win paper beats rock\n")
           game() #Loop so the game plays again
        else:
            print ("You lose" + " " + computer + " " + "beats" + " " + user)
            game() #Loop so the game plays again
            

    elif user == "scissors": # Logic to decide if you or the computer win
        if computer == "paper":
            print ("You win scissors beats paper\n")
            game() #Loop so the game plays again
        else:
            print ("You lose" + " " + computer + " " + "beats" + " " + user)
            game() #Loop so the game plays again



game() #Play the game
