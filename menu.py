#menu.py module


import pygame
import time



def menu_pygame():

    pygame.init()

    window_size = (1200, 800)

    screen = pygame.display.set_mode(window_size)
    bg_image = pygame.image.load("image.jpg")
    bg_image = pygame.transform.scale(bg_image, window_size)
    pygame.display.set_caption("menu")

    font = pygame.font.Font(None, 32)

    help_0 = " Help: "
    help_1 = " If you have a problem with running the game, please let me know"
    help_2 = " If I am not avaible with assissting you, please ask your peers or Mr.Tombs"
    help_3 = " For running the game, in the terminal, write python Hangman.py to run the code"
    rules_1 = "These are rules of the game:"
    rules_2 = "1: You can't get help from people or from technology"
    rules_3 = "2: One player plays at a time"
    rules_4 = "3: You can't search the words up"


    menu_label = font.render("Wellcome to HANGMAN GAME ", True, (255, 255, 255))
    rules_label = font.render("Press Enter for rules! ", True, (0, 255, 255))
    help_label = font.render("Press Tab for help! ", True, (0, 255, 255))
    game_label = font.render("Press any other key for continue to game! ", True, (0, 255, 255))
    
    screen.blit(bg_image,(0,0))
    screen.blit(menu_label, (450,25))
    screen.blit(rules_label, (50, 250))
    screen.blit(help_label, (50, 500))
    screen.blit(game_label, (50, 750))

    

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_TAB:
                    message_0 = font.render(help_0, True, (255, 255, 255))
                    screen.blit(message_0, (50, 550))
                    message_1 = font.render(help_1, True, (255, 255, 255))
                    screen.blit(message_1, (50, 600))
                    message_2 = font.render(help_2, True, (255, 255, 255))
                    screen.blit(message_2, (50, 650))
                    message_3 = font.render(help_3, True, (255, 255, 255))
                    screen.blit(message_3, (50, 700))
                elif event.key == pygame.K_RETURN:
                    message_1 = font.render(rules_1, True, (255, 255, 255))
                    message_2 = font.render(rules_2, True, (255, 255, 255))
                    message_3 = font.render(rules_3, True, (255, 255, 255))
                    message_4 = font.render(rules_4, True, (255, 255, 255))

                    screen.blit(message_1, (50, 300))
                    screen.blit(message_2, (150,350))
                    screen.blit(message_3, (150,400))
                    screen.blit(message_4, (150,450))

        
                else:
                    #message = font.render(rules, True,
                      #                      (255, 255, 255))
                    #screen.blit(message, (50, 150))
                    running = False
                    
          

        pygame.display.flip()

    #time.sleep(3)
    pygame.quit()