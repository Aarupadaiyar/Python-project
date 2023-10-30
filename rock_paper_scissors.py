rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
human=int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. "))
computer=random.randint(0,2)
print(f"computer choose {computer}")
game=[rock,paper,scissors]
print(game[human])
print(game[computer])

if computer==0 and human==2:
  print("You lose!")
elif computer > human:
  print("You lose!")
elif (human > computer) or (human==0 and computer==2):
  print("You win!")
elif human==computer:
  print("It is a tie!")
else:
  print("You entered a invalid number so hell get out! you lose!")
Print("Try one more time dude :)")