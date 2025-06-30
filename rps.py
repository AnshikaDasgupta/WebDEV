print("Let's Play Rock Paper Scissors!")
import random
options = ["Rock","Paper","Scissors"]
computer = random.choice(options)
# choice = input("Enter choice(Rock,Paper,Scissors): ")

# if choice == computer:
#     print("match draw")
# elif (choice == "Scissors" and computer == "Paper") or (choice == "Rock" and computer == "Scissors") or (choice == "Paper" and computer == "Rock"):
#     print("Yippee! You won!")
# else: 
#     print("You lost")

def play():
  computer = random.choice(options)
  choice = input("Enter choice(Rock,Paper,Scissors): ")

  if choice == computer:
    print("match draw")
  elif (choice == "Scissors" and computer == "Paper") or (choice == "Rock" and computer == "Scissors") or (choice == "Paper" and computer == "Rock"):
    print("Yippee! You won!")
  else: 
    print("You lost")

while True:
    ready = input("Are you ready?(type Y or N)")
    if ready == "Y":
        play()
    else:
        print("bye byee!")
        break