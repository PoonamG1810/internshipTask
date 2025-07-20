import random

# List of 5 predefined words
word_list = ["hangman", "assumption", "contradiction", "implication", "ranking"]

# Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a masked version of the word (e.g., "_ _ _ _ _")
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses. Good luck!\n")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("✅ Correct!\n")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!\n")

# End of game
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over. The word was:", secret_word)
