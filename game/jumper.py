
class Jumper:
    """The person guessing for the hidden word. 
    
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
        self._parachute = [" ▁▁▁▁▁ ",
                           "╱▁▁▁▁▁╲",
                           "╲     ╱",
                           " ╲   ╱",
                           "   0 ",
                           "  ╱|╲",
                           "  ╱ ╲",
                           "",
                           "^^^^^^^"]
        self._wrong_guesses = 0
        self._max_wrong_guesses = 5
        
        
    def update_parachute(self, wrong_guess):    
        """Removes a line from the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._wrong_guesses = wrong_guess
        if self._wrong_guesses < self._max_wrong_guesses:
            self._parachute.pop(0)
        elif self._wrong_guesses == self._max_wrong_guesses:
            self._parachute[0].replace("   0 ", "   x ")
        

    def has_lost(self):
        """Checks whether the Jumper lost the game.
        
        Args:
            self (Jumper): An instance of Jumper.
        
        Return:
            boolean: true if the Jumper lost.
        """
        if self._wrong_guesses == self._max_wrong_guesses:
            return True