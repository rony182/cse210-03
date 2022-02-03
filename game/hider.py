import random

class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _words (List[str]): List of possible words.
        _secret_word (str): Word that the player has to guess.
        _guesses (str): String representation of guesses.
        _chosen_letters (List[str]): List of letter that the player already chose.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        pass

    def check_guess(self, letter):
        """Checks if the letter is within the chosen word.

        Args:
            self (Hider): An instance of Hider.
            letter (str): Letter that the player chose.
        
        Return:
            str: String representation of guesses.
        """
        pass

    def _add_chosen_letter(self, letter):
        """Adds the player's chosen letter to the list

        Args:
            self (Hider): An instance of Hider.
            letter (str): Letter that the player chose.
        """
        pass

    def is_found(self):
        """Checks if the secret word was found.

        Args:
            self (Hider): An instance of Hider.

        Return:
            boolean: true if is was found.
        """
        pass