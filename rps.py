import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"

def playagain():
    "output: randomly plays rps"
    play = random.randint(0,1)
    if play == 1:
      return True
    else:
      print("Thanks for playing!")
      return False

#rps whileloop
#def rps(computer, user):
#    play = True
#    while play == True:
#      computer = choose_rps()
#      print(f"Computer chose {computer}.")
#      user = choose_rps()
#      print(f"User chose {user}.")

#      if computer == user:
#          print('It\'s a tie!')
#      elif computer == 'rock':
#          if user == 'paper':
#            print('user wins!')
#          else:
#            print('computer wins')
#      elif computer == 'paper':
#          if user == 'scissors':
#            print('user wins!')
#          else:
#            print('computer wins')
#      elif computer == 'scissors':
#          if user == 'rock':
#            print('user wins')
#          else:
#            print('computer wins')
#      print("......................................")
#      play = playagain()

#rps for loop
def rps(computer, user):
    for play in range(2):
      computer = choose_rps()
      print(f"Computer chose {computer}.")
      user = choose_rps()
      print(f"User chose {user}.")

      if computer == user:
          print('It\'s a tie!')
      elif computer == 'rock':
          if user == 'paper':
            print('user wins!')
          else:
            print('computer wins')
      elif computer == 'paper':
          if user == 'scissors':
            print('user wins!')
          else:
            print('computer wins')
      elif computer == 'scissors':
          if user == 'rock':
            print('user wins')
          else:
            print('computer wins')
      print("......................................")

#rps(computer, user)
