import hangman_art as art
import hangman_words as words
import random
import os


# Functions
def update_ui(n, msg):
    global display_word
    display_word = " ".join(display_list)
    global ui
    ui = f"{art.logo}\n\n{msg}\n{art.stages[n]}\n{display_word}"


def print_ui():
    # Testing code
    # print(f'Pssst, the solution is {chosen_word}.')
    print(f"\n{ui}\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables
chosen_word = (random.choice(words.word_list)).upper()
word_length = len(chosen_word)
lives = 6
guessed_letters = []
incorrect_letters = []

# Create blanks for each letter in the word
display_list = []
for letter in chosen_word:
    display_list.append("_")
    update_ui(lives, "")

# Loop while there is an undersdcore in the display word
while "_" in display_word:
    # Print all elements of the game
    print_ui()
    # Ask user to input a letter
    guess = input("Guess a letter: ").upper()
    # Clear the screen
    clear_screen()
    # Clear the current message, if any exists
    message = ""

    # Add guessed letter to list, if it does not exist
    if guess in guessed_letters:
        message = f"The letter '{guess}' has already been guessed"
    else:
        guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        for i in range(word_length):
            # Update display word with correctly guessed letter
            if chosen_word[i] == guess:
                display_list[i] = guess
                update_ui(lives, message)
    else:
        if guess in incorrect_letters:
            # Append already guessed message and ask for another letter
            message += f"\nThe letter '{guess}'' is not in the word"
            update_ui(lives, message)
            continue
        else:
            # Add guess to incorrect letters list
            incorrect_letters.append(guess)
            message = f"The letter '{guess}' is not in the word"
            # Reduce life by one
            lives -= 1
            if lives == 0:
                # End the game if there are no more lives
                break
            else:
                # Otherwise update the UI with the next stage image
                update_ui(lives, message)

if "_" in display_word:
    # Display losing message if there are unsolved letters
    message = f"You died! The word was: {chosen_word}"
else:
    # Otherwise, display the winning message
    message = "Congratulations! You won!"
update_ui(lives, message)
print_ui()
