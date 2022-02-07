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
        
        self._words =['cheese', 'summer', 'holiday', 'computer', 'mother', 'father', 'carpet']
        self._secret_word=''
        self._guesses=''
        self.chosen_letters=['']    # This should change for self._chosen_letters = [] otherwise [''] is not an empty list
        
    def choose_secret_word(self):
        """Choose the secret word from the list of possible words.

        Args:
            self (Hider): An instance of Hider.
            
        Return:
            str: String representation of the word chosen.
        """
        self._secret_word= random.choice(self._words)
        # Initialize _guesses with as many _ as the _secret_word's length
        self._guesses = '_' * len(self._secret_word)
        return self._secret_word
        
    
    def check_guess(self, letter):
        """Checks if the letter is within the chosen word.

        Args:
            self (Hider): An instance of Hider.
            letter (str): Letter that the player chose.
        
        Return:
            str: String representation of guesses.
        """
        # Instead of this
        list_of_letters=list(self._secret_word)
        for i in range(len(list_of_letters)):
            if list_of_letters[i]==letter:
                founded=str(i)  # i is an int
                self._guesses+=founded  # this will append a number, not a letter
            else:
                self._guesses+='_ '
                
        # We can do this
        for i, c  in enumerate(self._secret_word):
            # i is the index, c is the letter
            if letter == c:
                self._guesses[i] = c
            
        return self._guesses

    def add_chosen_letter(self, letter):
        """Adds the player's chosen letter to the list

        Args:
            self (Hider): An instance of Hider.
            letter (str): Letter that the player chose.
        """
        self.chosen_letters.append(letter)
        return self.chosen_letters

    def is_found(self):
        """Checks if the secret word was found.

        Args:
            self (Hider): An instance of Hider.

        Return:
            boolean: true if is was found.
        """
        pass
