import random

class ai:

    def __init__(self):
    
        self.name = 'computer'
        
    def generate_name(self):
        return 'computer'
        
    def generate_choice(self):
        choice = random.randrange(1,3)
        if choice == 1:
             print("rock")
        elif choice == 2:
            print("paper")
        else:
            print("scissors")
        return choice
        
        