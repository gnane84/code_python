import random                           # Used to pick a random word
from hangman_word import word_list      # List of possible words (your custom module/file)
from hangman_art import stages          # ASCII art stages (your custom module/file)

lives = 6                               # Player starts with 6 lives (index matches stages list)

chosen_word = random.choice(word_list)  # Randomly choose a word from the list
print(chosen_word)                      # DEBUG: prints the chosen word (remove this in final game)

# Create the starting placeholder like "_____"
placeholder = ""
word_length = len(chosen_word)          # Length of the word to guess
for position in range(word_length):     # Build "_" for each letter position
    placeholder += "_"
print(f"word to guess : {placeholder}") # Show blank word to the user

game_over = False                       # Controls the main game loop
correct_letters = []                    # Stores letters the user has guessed correctly

# Keep looping until player wins or loses
while not game_over:
    # Show how many lives are remaining
    print(f"************you {lives}/6 LIVES LEFT************")

    # Get one letter guess from the user and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # If user already guessed a correct letter, remind them
    if guess in correct_letters:
        print(f"you already guessed {guess}")

    display = ""                        # This will build the updated word display for this round

    # Go through every letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            # If the guessed letter matches, reveal it and store it as correct
            display += letter
            correct_letters.append(letter)   # Save correct guess for future rounds
        elif letter in correct_letters:
            # If this letter was guessed earlier, keep showing it
            display += letter
        else:
            # Otherwise keep it hidden
            display += "_"

    print(display)                      # Print the current progress (e.g., "_ a _ _")

    # If guess is not in the chosen word, lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If no lives remain, game ends (loss)
        if lives == 0:
            game_over = True
            print(f"********** IT WAS {chosen_word}! You Lose*********")

    # If there are no "_" left, the user has guessed the whole word (win)
    if "_" not in display:
        game_over = True
        print(f"**************You won!*************")

    # Print the hangman picture that matches the remaining lives
    print(stages[lives])
