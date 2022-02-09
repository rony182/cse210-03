from game.terminal_service import TerminalService
from game.hider import Hider
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        new_letter (str): The string that contains the letter from the user input.
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._new_letter = ""
        self._hider = Hider()
        self._is_playing = True
        self._player = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by setting a hidden word and running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._hider.choose_secret_word()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets a letter from the user to start the game.

        Args:
            self (Director): An instance of Director.
        """
        self._new_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        

    def _do_updates(self):
        """Keeps track of the letter the user inputs and updates the parachute.

        Args:
            self (Director): An instance of Director.
        """
        self._hider.check_guess(self._new_letter)
        self._hider.add_chosen_letter(self._new_letter)
        self._player.update_parachute(self._hider.get_num_wrong_guesses())
        if self._hider.is_found() or self._player.has_lost():
            self._is_playing = False
        
        
    def _do_outputs(self):
        """Calls the Terminal Service to display the hidden word (as it is revealed),
         the parachute, and the chosen letters for the user to see.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._hider.get_guesses())
        self._terminal_service.display_parachute(self._player.get_parachute())
        self._terminal_service.write_text(f"Letters used: {self._hider.get_chosen_letters()}")
        if not self._is_playing:
             self._terminal_service.write_text("Game over, thanks for playing. ")
