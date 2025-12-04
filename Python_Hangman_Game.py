import random
import string
from typing import List, Set

class Hangman:
    def __init__(self, word_list: List[str], max_attempts: int = 6):
        """
        Initialize the Hangman game.
        
        Args:
            word_list: List of words to choose from
            max_attempts: Maximum allowed wrong attempts (default: 6)
        """
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.reset_game()
    
    def reset_game(self) -> None:
        """Reset the game state for a new game."""
        self.secret_word = random.choice(self.word_list).upper()
        self.guessed_letters: Set[str] = set()
        self.attempts_left = self.max_attempts
        self.game_over = False
        self.won = False
    
    @property
    def current_state(self) -> str:
        """
        Get the current state of the word being guessed, with underscores for unguessed letters.
        
        Returns:
            The current word state (e.g., "H _ L L O")
        """
        return ' '.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.secret_word
        )
    
    @property
    def remaining_letters(self) -> str:
        """
        Get letters that haven't been guessed yet.
        
        Returns:
            String of unguessed letters in alphabetical order
        """
        return ' '.join(
            sorted(
                set(string.ascii_uppercase) - self.guessed_letters
            )
        )
    
    def make_guess(self, letter: str) -> bool:
        """
        Process a player's guess.
        
        Args:
            letter: The letter being guessed (case-insensitive)
        
        Returns:
            True if guess was valid and processed, False otherwise
        
        Raises:
            ValueError: If game is already over or letter is invalid
        """
        if self.game_over:
            raise ValueError("Game is already over")
        
        letter = letter.upper()
        
        # Validate input
        if len(letter) != 1:
            print("Please enter a single letter.")
            return False
        if letter not in string.ascii_letters:
            print("Please enter a valid letter (A-Z).")
            return False
        if letter in self.guessed_letters:
            print(f"You've already guessed '{letter}'. Try another letter.")
            return False
        
        # Process the guess
        self.guessed_letters.add(letter)
        
        if letter not in self.secret_word:
            self.attempts_left -= 1
            print(f"Sorry, '{letter}' is not in the word.")
        else:
            print(f"Good guess! '{letter}' is in the word.")
        
        # Check game status
        self._check_game_status()
        return True
    
    def _check_game_status(self) -> None:
        """Check if the game has been won or lost."""
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.game_over = True
            self.won = True
        elif self.attempts_left <= 0:
            self.game_over = True
            self.won = False
    
    def display_status(self) -> None:
        """Display the current game status."""
        print("\n" + "=" * 30)
        print(f"Word: {self.current_state}")
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {' '.join(sorted(self.guessed_letters))}")
        print(f"Available letters: {self.remaining_letters}")
        
        # Display hangman progress (optional visual)
        self._draw_hangman()
    
    def _draw_hangman(self) -> None:
        """Optional: Draw hangman progress based on attempts left."""
        stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            """
        ]
        print(stages[self.max_attempts - self.attempts_left])


def choose_difficulty() -> int:
    """Let player choose game difficulty."""
    print("Choose difficulty:")
    print("1. Easy (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")
    
    while True:
        choice = input("Enter choice (1-3): ")
        if choice in {'1', '2', '3'}:
            return {'1': 8, '2': 6, '3': 4}[choice]
        print("Invalid input. Please enter 1, 2, or 3.")


def main():
    # Word list categorized by difficulty
    word_lists = {
        'easy': ['apple', 'happy', 'water', 'music', 'pizza'],
        'medium': ['python', 'hangman', 'jazz', 'quasar', 'xylophone'],
        'hard': ['awkward', 'bagpipes', 'espionage', 'ivory', 'oxygen']
    }
    
    print("Welcome to Hangman!")
    
    while True:
        # Set up game
        difficulty_attempts = choose_difficulty()
        all_words = word_lists['easy'] + word_lists['medium'] + word_lists['hard']
        game = Hangman(all_words, difficulty_attempts)
        
        # Game loop
        while not game.game_over:
            game.display_status()
            
            # Get valid input
            while True:
                guess = input("Guess a letter: ").strip()
                if game.make_guess(guess):
                    break
        
        # Game over
        game.display_status()
        if game.won:
            print(f"\nCongratulations! You guessed '{game.secret_word}' correctly!")
        else:
            print(f"\nGame over! The word was '{game.secret_word}'.")
        
        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        print("\n" + "=" * 30 + "\n")


if __name__ == "__main__":
    main()