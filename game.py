# I acknowledge the use of ChatGPT (GPT-5.1, OpenAI) to assist me with ideas and structure.
# I have reviewed and tested the code myself.
import random

def play_game():
    print("Welcome to the Guess the Number game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have a maximum of 10 attempts.")

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a whole number between 1 and 100.")
            continue

        guess = int(guess_input)
        attempts += 1

        # check that guess is in the correct range
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        # check if player ran out of attempts
               # check if player ran out of attempts
        if attempts == 10 and guess != secret_number:
            print("You have used all 10 attempts. Game over!")
            print("The correct number was:", secret_number)
            break


        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            guessed = True

def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Play again? (y/n): ")

    print("Thanks for playing the game!")

if __name__ == "__main__":
    main()
