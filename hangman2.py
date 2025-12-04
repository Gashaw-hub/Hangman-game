import random

# Hangman visual stages
HANGMAN_STAGES = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

# Logo
LOGO = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Word list
WORD_LIST = [
    'abruptly', 'awkward', 'bagpipes', 'buzzing', 'cycle', 'dizzying', 'equip', 'fjord',
    'galaxy', 'hyphen', 'jackpot', 'kayak', 'mnemonic', 'oxygen', 'pixel', 'quartz',
    'rhythm', 'strength', 'topaz', 'vortex', 'wizard', 'xylophone', 'yummy', 'zodiac'
]


# Functions
def choose_word(difficulty):
    """Selects a word based on difficulty."""
    if difficulty == "easy":
        return random.choice([w for w in WORD_LIST if len(w) <= 5])
    elif difficulty == "medium":
        return random.choice([w for w in WORD_LIST if 6 <= len(w) <= 7])
    else:  # hard
        return random.choice([w for w in WORD_LIST if len(w) > 7])


def print_status(word_progress, guessed_letters, wrong_guesses, max_wrong):
    print(f"\nWrong guesses: {wrong_guesses}/{max_wrong}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Word: " + " ".join(word_progress))
    print(HANGMAN_STAGES[wrong_guesses])


def get_valid_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"⚠️ You've already guessed '{guess}'.")
        else:
            return guess


def play_game():
    print(LOGO)
    print("🕹️ Welcome to Hangman!\n")
    score = 0

    # Difficulty selection
    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("❗ Invalid input. Choose difficulty (easy / medium / hard): ").lower()

    chosen_word = choose_word(difficulty)
    word_progress = ["_"] * len(chosen_word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_STAGES) - 1

    while True:
        print_status(word_progress, guessed_letters, wrong_guesses, max_wrong)
        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✅ Good guess!")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_progress[i] = guess
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1

        if "_" not in word_progress:
            print_status(word_progress, guessed_letters, wrong_guesses, max_wrong)
            print("🎉 You WON! 🎉")
            score += 1
            break

        if wrong_guesses == max_wrong:
            print_status(word_progress, guessed_letters, wrong_guesses, max_wrong)
            print("💀 Game Over! The word was:", chosen_word)
            break

    print(f"🏆 Your score: {score}")
    return score


# Main game loop
def main():
    total_score = 0
    while True:
        total_score += play_game()
        again = input("🔁 Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print(f"🎯 Final Score: {total_score}")
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
