class human:

    def __init__(self):
        pass
                
        
    def give_name(self,playerName):
        name = input(playerName + ": what is your name? \n")
        return name
           
    def make_choice(self,playerName):
        guess = input(playerName + ": enter rock, paper, or scissors.\n")
        if guess == "rock":
            choice = 1
        elif guess == "paper":
            choice = 2
        else:
            choice = 3
        return choice