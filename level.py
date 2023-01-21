import pygame 


def select_level():


    running = True
    selected_level = "easy"

    

 #initializes the pygame screen
    pygame.init()

    font = pygame.font.Font(None, 32)

 #This just sets the boundary for the login page size
    window_size = (800, 600)
    icon_size = (100,150)

 #This just uses an image fron image_1 file and it creates it on the login page
    screen = pygame.display.set_mode(window_size)
    # bg_image = pygame.image.load("image_1.jpg")
    # bg_image = pygame.transform.scale(bg_image, window_size)
    pygame.display.set_caption("Select level")

    icon_image_e_0 = pygame.image.load("Easy.jpg")
    icon_image_e = pygame.transform.scale(icon_image_e_0, icon_size)
    icon_image_m_0 = pygame.image.load("medium.jpg")
    icon_image_m = pygame.transform.scale(icon_image_m_0, icon_size)
    icon_image_h_0 = pygame.image.load("hard.jpg")
    icon_image_h = pygame.transform.scale(icon_image_h_0, icon_size)


    select_level_label = font.render("Which level do you choose? (easy/medium/hard):", True, (255, 255, 255))
    screen.blit(select_level_label, (100, 100))
    


    icon_rec_e = icon_image_e.get_rect()
    icon_rec_m = icon_image_m.get_rect()
    icon_rec_h = icon_image_h.get_rect()

    icon_rec_e.x = 200
    icon_rec_e.y = 200

    icon_rec_m.x = 400
    icon_rec_m.y = 200

    icon_rec_h.x = 600
    icon_rec_h.y = 200


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if icon_rec_e.collidepoint(event.pos):
                    #print("The easy icon clicked!")
                    selected_level = "easy"
                    running = False
                elif icon_rec_m.collidepoint(event.pos):
                    #print("The medium icon clicked!")
                    selected_level = "medium"
                    running = False
                elif icon_rec_h.collidepoint(event.pos):
                    #print("The hard icon clicked!")
                    selected_level = "hard"
                    running = False

        
            

        #It updates the screen
        pygame.display.flip()

        screen.blit(icon_image_e,icon_rec_e)
        screen.blit(icon_image_m,icon_rec_m)
        screen.blit(icon_image_h,icon_rec_h)


        pygame.display.update()

    #It will freeze the screen for 3 seconds

    #Closing login screen
    pygame.quit()

    return selected_level


    #It will return the result and username of the code


#select_level()
