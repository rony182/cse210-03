class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
        

    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(f"\n{text}\n")


    def display_parachute(self, parachute):
        """Displays the given list (parachute) on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (List[str]): The parachute to display.
        """
        for i in range(len(parachute)):
            print(f"{parachute[i]}")
