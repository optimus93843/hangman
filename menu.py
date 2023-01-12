import pygame
import time



def menu_pygame():

    pygame.init()

    window_size = (600, 400)

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("menu")

    font = pygame.font.Font(None, 32)

    help = " help "
    rules = "These are rules of the game"

    menu_label = font.render("Wellcome to HANGMAN GAME ", True, (0, 0, 255))
    rules_label = font.render("Press Enter for rules! ", True, (255, 255, 255))
    help_label = font.render("Press Tab for help! ", True, (255, 255, 255))
    game_label = font.render("Press any other key for continue to game! ", True, (255, 255, 255))

    screen.blit(menu_label, (150,25))
    screen.blit(rules_label, (50, 150))
    screen.blit(help_label, (50, 250))
    screen.blit(game_label, (50, 350))



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_TAB:
                    message = font.render(help, True,
                                            (100, 100, 100))
                    screen.blit(message, (50, 300))
                elif event.key == pygame.K_RETURN:
                    message = font.render(rules, True,
                                            (100,100,100))
                    screen.blit(message, (50, 200))
                else:
                    #message = font.render(rules, True,
                      #                      (255, 255, 255))
                    #screen.blit(message, (50, 150))
                    running = False
                    
          

        pygame.display.flip()

    #time.sleep(3)
    pygame.quit()