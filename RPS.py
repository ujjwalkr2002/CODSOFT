import random

print("Welcome to Rock Paper Scissors Game:\n")

print("""Game Rule :-
Rock wins against Scissors.
Scissors wins against Paper.
Paper wins against Rock.\n""")

print("""1. Rock
2. Paper 
3. Scissors \n""")

user_score = 0
comp_score = 0
tie = 0

while True:
    user_choice = int(input("Enter your choice (1-3): "))
    
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please choose a number between 1 and 3.")
        continue
    
    comp_choice = random.randint(1, 3)
    print("Computer choice is:", comp_choice)
    
    if user_choice == comp_choice:
        print("It's a tie.")
        tie += 1
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        print("You win.")
        user_score += 1
    else:
        print("Computer wins.")
        comp_score += 1

    print(f"Scoreboard - You: {user_score}, Computer: {comp_score}, Ties: {tie}\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
