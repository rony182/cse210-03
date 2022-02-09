import random


class Hider:
    """The person hiding a word from the player (Jumper). 
    
    The responsibility of Hider is to keep track of it's hidden word and, decide whether the player's inputs
    match the hidden word. 
    
    Attributes:
        _words (List[str]): List of possible words.
        _secret_word (str): Word that the player has to guess.
        _guesses (str): String representation of guesses.
        _chosen_letters (List[str]): List of letters that the player chose.
        _wrong_guesses (int): Counter that keeps track of the wrong guesses.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        
        self._words =['cheese', 'summer', 'holiday', 'computer', 'mother', 'father', 'carpet']
        self._secret_word=''
        self._guesses=''
        self._chosen_letters=[]
        self._wrong_guesses = 0

    def choose_secret_word(self):
        """Choose the secret word from the list of possible words.

        Args:
            self (Hider): An instance of Hider.
            
        Return:
            str: String representation of the hidden word.
        """
        self._secret_word= random.choice(self._words)
        self._guesses = '_' * len(self._secret_word)

        return self._secret_word
        
    
    def check_guess(self, letter):
        """Checks if the letter is within the hidden word.

        Args:
            self (Hider): An instance of Hider.
            letter (str): The letter chosen by the player.
        """

        aux = list(self._guesses)

        for i, c in enumerate(self._secret_word):
            if letter == c:
                aux[i] = c
        self._guesses = "".join(aux)

        if letter not in self._secret_word:
            self._wrong_guesses += 1
        

    def add_chosen_letter(self, letter):
        """Adds the player's chosen letter to the list.

        Args:
            self (Hider): An instance of Hider.
            letter (str): The letter chosen by the player.
        
        Returns:
            _chosen_letters (List[str]): List of letters that the player chose.

        """
        self._chosen_letters.append(letter)

    
    def get_chosen_letters(self):
        """Returns a List of letters chosen by the player throughout the game."""

        return self._chosen_letters


    def get_num_wrong_guesses(self):
        """Returns the number of wrong guesses that the player has."""

        return self._wrong_guesses


    def get_guesses(self):
        """Returns a string representation of guesses. (Ex: c_ee_e)"""

        return self._guesses 


    def is_found(self):
        """Checks if the secret word was found.

        Args:
            self (Hider): An instance of Hider.

        Return:
            boolean: true if is was found.
        """
        
        return self._secret_word == self._guesses