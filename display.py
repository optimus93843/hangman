import pygame 
import time


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


def display_scores(data):

  pygame.init()
  window_size = (1000,800)

  screen = pygame.display.set_mode(window_size)
  bg_image = pygame.image.load("image_2.jpg")
  bg_image = pygame.transform.scale(bg_image, window_size)
  pygame.display.set_caption("Let's see who's winning")

  
  font = pygame.font.Font(None, 32)

  username_label = font.render("User Name ", True, (255,255,255))
  score_label = font.render("Score ", True, (255, 255, 255))

  username_line = font.render("----------------", True, (100,100,100))
  score_line = font.render("--------", True, (100,100,100))

  screen.blit(bg_image,(0,0))
  screen.blit(username_label, (50, 50))
  screen.blit(score_label, (250, 50))
  screen.blit(username_line, (50, 65))
  screen.blit(score_line, (250, 65))
  
  running = True
  counter = 1
  for user in data:
    username = font.render(user , True, (255,0,0))
    screen.blit(username, (50,65 + counter*50))
    score = font.render(data[user][:-1] , True, (255,0,0))
    screen.blit(score, (275,65 + counter*50))
    counter += 1
    #     print("User name: " + score + '---'+"Score: " +  score_board[score] )

  while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

  pygame.quit()










