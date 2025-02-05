import random

# List of words to guess
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Choose a random word
word = random.choice(words)

# Initialize variables
guessed_letters = []
guessed_word = ['_'] * len(word)
tries = 6

# Hangman stages (for visual representation)
hangman_stages = [
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
         ===
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
         ===
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
         ===
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
         ===
    """,
    """
      -----
      |   |
      O   |
          |
          |
         ===
    """,
    """
      -----
      |   |
          |
          |
          |
         ===
    """
]

# Function to display the current game state
def display_game():
    print(hangman_stages[tries])  # Show hangman stage
    print(f"Word: {' '.join(guessed_word)}")
    print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    print(f"Tries Left: {tries}\n")

# Game loop
while '_' in guessed_word and tries > 0:
    display_game()
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter!\n")
        continue
    if guess in guessed_letters:
        print("⏳ You've already guessed this letter! Try another one.\n")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Incorrect! Tries left: {tries}\n")

# Game over messages
display_game()
if '_' not in guessed_word:
    print("🎉 Congratulations! You guessed the word! 🎉\n")
else:
    print(f"💀 Game over! The word was: {word} 💀\n")
