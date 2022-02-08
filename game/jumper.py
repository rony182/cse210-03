import random

class Jumper:
    """The person looking for the Hider. 
    
    The responsibility of a Jumper is to keep track of its parachute.
    
    Attributes:
        _parachute (List[str]): String representation of the Jumper's parachute.
        _wrong_guesses (int): Counter that keeps track of the wrong guesses.
        _max_wrong_guesses (int): Maximum number of possible wrong guesses (5).
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        words = ["python", "anaconda", "snake", "cobra", "constrictor",  "miniconda"]
        word = random.choice(words)
        self._letter = list(word)
 

    def get_parachute(self):
        """Gets the current status of the parachute.
        
        Returns:
            List[str]: String representation of the Jumper's parachute.
        """
        return self._letter
        
    def update_parachute(self):    
        """Removes a line from the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        max_wrong_guess = 5
        wrong_guess = 0
        guess = ""
        if guess not in self._letter and wrong_guess == 0:
            print(f" --- \n /___\ \n \   / \n \  / ")
            print(f" o \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1    
        elif guess not in self._letter and wrong_guess == 1:
            print(f"     \n /___\ \n \   / \n \  / ")
            print(f" o \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1
        elif guess not in self._letter and wrong_guess == 2:
            print(f"     \n       \n \   / \n \  / ")
            print(f" o \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1
        elif guess not in self._letter and wrong_guess == 3:
            print(f"     \n       \n       \n \  / ")
            print(f" o \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1
        elif guess not in self._letter and wrong_guess == 4:
            print(f"     \n       \n       \n      ")
            print(f" o \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1
        elif guess not in self._letter and wrong_guess == 5:
            print(f"     \n       \n       \n      ")
            print(f" x \n / | \ \n /\ \n ")
            print(f"^^^^^^")
            wrong_guess += 1
        else:
            print(f"Game over")     


    def has_lost(self):
        """Checks whether the Jumper lost the game.
        
        Args:
            self (Jumper): An instance of Jumper.
        
        Return:
            boolean: true if the Jumper lost.
        """
        pass