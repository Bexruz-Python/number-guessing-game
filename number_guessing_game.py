import random


def user_guesses():
    print("Number Guessing Game")
    print("I have chosen a number between 1 and 10. Try to guess it!")

    attempts = 0
    secret_number = random.randint(1, 10)

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.\n")
            break
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a bigger number.")


def computer_guesses():
    print("Now think of a number between 1 and 10.")
    print("I will try to guess it!")

    low = 1
    high = 10
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is: {guess}")
        feedback = input("Is it (+) too high, (-) too low, or (=) correct? ").strip()

        if feedback == "=":
            print(f"I guessed your number in {attempts} attempts!\n")
            break
        elif feedback == "+":
            low = guess + 1
        elif feedback == "-":
            high = guess - 1


def main():
    while True:
        user_guesses()
        computer_guesses()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Game over. Thanks for playing!")
            break


main()
