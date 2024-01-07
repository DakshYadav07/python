import random
def basic():
    choices=['rock','paper','scissor']
    comp_choice=random.choice(choices)
    while True: 
        user_choice = input("Select Your Move (Rock, Paper, Scissor): ").lower()
        if user_choice in choices:  
            break  
        else: 
            print("INVALID! Choose Between Rock, Paper, Scissor")
    print(f"Your Move Was {user_choice} and Computer's was {comp_choice}")
    if comp_choice == user_choice:
        print("It's A Tie")
        return 0
    elif (user_choice == 'rock' and comp_choice == 'scissor')or(user_choice == 'scissor' and comp_choice == 'paper')or(user_choice == 'paper' and comp_choice == 'rock'):
        print("You Win!:)")
    else :
        print("You Lose!:(")
while True:
    basic()
    again = input("Do You Want To Continue?(yes/no): ")
    if again.lower() != "yes":
        print("Thanks For Playing :)")
        break