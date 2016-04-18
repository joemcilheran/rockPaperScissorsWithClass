import human
import ai
class game:

    def __init__(self):
        pass
        
   
    def get_result(self,playerOneName,playerTwoName,playerOne,playerTwo):
        playerOneChoice = playerOne.make_choice(playerOneName)
        if playerTwoName == "computer":
           playerTwoChoice = playerTwo.generate_choice()
        else:
           playerTwoChoice = playerTwo.make_choice(playerTwoName)
           
        if (playerOneChoice == playerTwoChoice):
            print("TIE")
            return "TIE"
        elif (playerOneChoice - playerTwoChoice)%3 == 1:
            print(playerOneName + " wins game! \n")
            return playerOneName
        else:
            print(playerTwoName + " wins game! \n")
            return playerTwoName