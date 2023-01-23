#menu.py module


import pygame  #Import pygame is just imports all the avaible pygame modules
import time    #What the import time does it takes 3 seconds after when you login with your username and password to open up a new page 



#This for the menu 
def menu_pygame():

 #initializes the pygame screen
    pygame.init()

 #This just sets the boundary for the menu page size
    window_size = (1200, 800)

 #This just uses an image fron image.jpg file and it creates it on the login page
    screen = pygame.display.set_mode(window_size)
    bg_image = pygame.image.load("image.jpg")
    bg_image = pygame.transform.scale(bg_image, window_size)
    pygame.display.set_caption("menu")

#This just sets the default font for all the texts 
    font = pygame.font.Font(None, 32)

 #This is for the rules and helping the user how to play 
    help_0 = " Help: "
    help_1 = " If you have a problem with running the game, please let me know"
    help_2 = " If I am not avaible with assissting you, please ask your peers or Mr.Tombs"
    help_3 = " For running the game, in the terminal, write python Hangman.py to run the code"
    rules_1 = "These are rules of the game:"
    rules_2 = "1: You can't get help from people or from technology"
    rules_3 = "2: One player plays at a time"
    rules_4 = "3: You can't search the words up"

 #This is just for fonts
    menu_label = font.render("Wellcome to HANGMAN GAME ", True, (255, 255, 255))
    rules_label = font.render("Press Enter for rules! ", True, (0, 255, 255))
    help_label = font.render("Press Tab for help! ", True, (0, 255, 255))
    game_label = font.render("Press any other key for continue to game! ", True, (0, 255, 255))
    
 #Puts an image on the login page
    screen.blit(bg_image,(0,0))

 #Copys content on one surface to other
    screen.blit(menu_label, (450,25))
    screen.blit(rules_label, (50, 250))
    screen.blit(help_label, (50, 500))
    screen.blit(game_label, (50, 750))

    
 #This means that when the page loads, the user can start clicking and writing
    running = True
    while running:
        

        #This is for the keys and for the color of the text 
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
                    
                    #Positioning of the message that will dipslayed in the menu page
                    screen.blit(message_1, (50, 300))
                    screen.blit(message_2, (150,350))
                    screen.blit(message_3, (150,400))
                    screen.blit(message_4, (150,450))

                #This is for if the user puts something random, it won't execute the code 
                else:
                    
                    running = False
                    
          
        #It updates the screen
        pygame.display.flip()

        #Closing login screen
    pygame.quit()