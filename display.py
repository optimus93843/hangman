import pygame #This Imports all the avaible pygame modules


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

    #Ends the function and returns the hangman lines
    return states[tries]


#This is for displaying the scoreboard
def display_scores(data):

  #This initializes the pygame
  pygame.init()

  #This is the parameters for the scoreboard page
  window_size = (1000,800)

  #This is for the background image to be set when you go into the scoreboard page
  screen = pygame.display.set_mode(window_size)
  bg_image = pygame.image.load("image_2.jpg")
  bg_image = pygame.transform.scale(bg_image, window_size)
  pygame.display.set_caption("Let's see who's winning")

  #This is the font for everything
  font = pygame.font.Font(None, 32)

  #This is for the colors of the username and score
  username_label = font.render("User Name ", True, (255,255,255))
  score_label = font.render("Score ", True, (255, 255, 255))

  #This is for the jotted line
  username_line = font.render("----------------", True, (100,100,100))
  score_line = font.render("--------", True, (100,100,100))

  #This is for the positioning of the labels
  screen.blit(bg_image,(0,0))
  screen.blit(username_label, (50, 50))
  screen.blit(score_label, (250, 50))
  screen.blit(username_line, (50, 65))
  screen.blit(score_line, (250, 65))
  
  #This shows the screen for the scoreboard
  running = True
  counter = 1

  #Shows all the score and username in each line
  for user in data:
    username = font.render(user , True, (255,0,0))
    screen.blit(username, (50,65 + counter*50))
    score = font.render(data[user][:-1] , True, (255,0,0))
    screen.blit(score, (275,65 + counter*50))
    counter += 1

  #This shows the score as long as we don't click on the red cross sign
  while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        #Allows for the screen to get updated
        pygame.display.flip()


  #This quits the screen 
  pygame.quit()










