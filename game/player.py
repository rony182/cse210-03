class Player:
    """The person looking for the Hider. 
    
    The responsibility of a Player is to keep track of its parachute.
    
    Attributes:
        _parachute (List[str]): String representation of the player's parachute.
        _wrong_guesses (int): Counter that keeps track of the wrong guesses.
        _max_wrong_guesses (int): Maximum number of possible wrong guesses (5).
    """

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): An instance of Player.
        """
        pass

    def get_parachute(self):
        """Gets the current status of the parachute.
        
        Returns:
            List[str]: String representation of the player's parachute.
        """
        pass
        
    def update_parachute(self):    
        """Removes a line from the parachute.

        Args:
            self (Player): An instance of Player.
        """
        pass

    def has_lost(self):
        """Checks whether the player lost the game.
        
        Args:
            self (Player): An instance of Player.
        
        Return:
            boolean: true if the player lost.
        """
        pass