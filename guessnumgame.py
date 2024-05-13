import random

secret_number = random.randint(1, 10)
max_attempts = 3

def welcome_message():
    print("\nWelcome to the number guessing game!")
    print(f'You have {max_attempts} attempts to guess the correct number')

def guess_recursive(attempt_left):
    guess = int(input('\nGuess the number (between 1 to 10): '))
    if guess == secret_number:
        print('Congratulations! You guessed the correct number.')
    else:
        print(f'Wrong guess! You have {attempt_left - 1} attempts left.')
        if attempt_left > 1:
            guess_recursive(attempt_left - 1)
        else:
            print(f'\nSorry, you failed to guess the number. The guessing number was {secret_number}')
            return
    print(f'Memory address of the secret number {secret_number} is: {id(secret_number)}')

welcome_message()
guess_recursive(max_attempts)
