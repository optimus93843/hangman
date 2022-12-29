# This function will display the hanging man
def display_hangman(tries):
    states = [  # head, torso, both arms, and both legs
        """
      -------------
      |        |
      |        O
      |       \\|/
      |        |
      |       / \\
      |
      ---
    """,
        # head, torso, both arms, and one leg
        """
      -------------
      |        |
      |        O
      |       \\|/
      |        |
      |       /
      |
      ---
    """,
        # head, torso, both arms
        """
      -------------
      |        |
      |        O
      |       \\|/
      |        |
      |       
      |
      ---
    """,
        # head, torso, one arm
        """
      -------------
      |        |
      |        O
      |       \\|
      |       
      |       
      |
      ---
    """,
        # head, torso
        """
      -------------
      |        |
      |        O
      |        |
      |        |
      |       
      |
      ---
    """,
        # head
        """
      -------------
      |        |
      |        O
      |      
      |        
      |       
      |
      ---
    """,
        # Initial empty state
        """
      -------------
      |        |
      |        
      |     
      |        
      |       
      |
      ---
    """
    ]

    return states[tries]
