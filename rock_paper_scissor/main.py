import random

def play():
     user = input("'r' is Rock,'p' is paper,'s' is scissor\n")
     computer_guess = random.choice(['r','s','p'])

     if computer_guess== user:
          return "it\'s a tie"
     if isWin(user,computer_guess):
          return "YOU WIN congratulation "
     return "Sorry ,You lost"
     
def isWin(player1,player2):
     if ( player1 =='r' and player2 =='s' ) or (player1 =='s' and player2 == 'p' ) or (player1 =='p' and player2 == 'r' ):
          return True

print(play())
          