import human
import ai
import game

class match:

    def __init__(self):
        pass    
        
    def keep_score(self,playerOneName,playerTwoName,playerOne,playerTwo):
        playerOneWins = []
        playerTwoWins = []
            
        while len(playerOneWins) < 3 and len(playerTwoWins) < 3:
            thegame = game.game()
            gameWinner = thegame.get_result(playerOneName,playerTwoName,playerOne,playerTwo)
            if gameWinner == playerOneName:
                playerOneWins.append(playerOneName)
            elif gameWinner == playerTwoName:
                playerTwoWins.append(playerTwoName)
        if len(playerOneWins) == 3:
            print(playerOneName + " wins the match! \n")
        elif len(playerTwoWins) == 3:
            print(playerTwoName + " wins the match! \n")
                    
        
    def play_with_one(self):
        playerOne = human.human()
        playerOneName = playerOne.give_name("PlayerOne")
        playerTwo = ai.ai()
        playerTwoName = playerTwo.generate_name()
        self.keep_score(playerOneName,playerTwoName,playerOne,playerTwo)
            
            
    def play_with_two(self):
        playerOne = human.human()
        playerOneName = playerOne.give_name("PlayerOne")
        playerTwo = human.human()
        playerTwoName = playerTwo.give_name("PlayerTwo")
        self.keep_score(playerOneName,playerTwoName,playerOne,playerTwo)       
    
    def begin(self):
        choice = input("Welcome to Rps. Would like to play with one player or two(1 or 2) \n")
        if choice == "1":
            self.play_with_one()
        else:
            self.play_with_two()
               
             
               
    
                    