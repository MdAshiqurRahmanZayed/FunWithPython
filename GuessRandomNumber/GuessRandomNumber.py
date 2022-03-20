import random

def guess(x):
     random_number = random.randint(1,x)
     guess = 0
     while random_number != guess:
          guess = int(input(f"Guess between 1 and {x} \n"))
          if guess < random_number:
               print("Sorry! guess again, too low")
          elif guess > random_number:
               print("Sorry! guess again, too high")
     
     print(f"Hurray you guesses the random number {random_number} ")

def computer_guess(x):
     low = 1
     high = x
     feedBack = ''
     while feedBack !='c':
          if low != high:
               guess_number = random.randint(low,high)
          else:
               guess_number = low
               
          feedBack = input(f"IS {guess_number} is too high(h),too low(l),correct (c) ") 
          
          if feedBack == "h":
               high = guess_number - 1
          elif feedBack == "l":
               low = guess_number + 1
          
               
     print(f"computer guessed your number {guess_number}, correctly")

computer_guess(1000)
# guess(10)
