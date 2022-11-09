#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def random_number():
    return random.randint(1, 101)

def check_border(user_number, final_number):
    if user_number < final_number:
        print("Too low.")
    else:
        print("Too high.")


number_of_attempts = 0
# number_of_guess = 0
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level == "hard":
    number_of_attempts = 5
elif difficulty_level == "easy":
    number_of_attempts = 10
else:
    print("You Entered a wrong answer")
final_answer = random_number()
print(f"Final Answer is {final_answer}")
flag = True
while number_of_attempts > 0 and flag:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    input_number = int(input("Make a guess: "))
    if input_number != final_answer:
        check_border(input_number, final_answer)
        number_of_attempts -= 1
        if number_of_attempts != 0:
            print("Guess Again.")
    
    else:
        flag = False

if number_of_attempts == 0  and input_number != final_answer:
    print(f"You've run out of guesses, you lose. The answer was {final_answer}.")
else:
    print(f"You got it! The answer was {final_answer}.")

