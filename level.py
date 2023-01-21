import pygame 


def select_level():


    running = True

 #initializes the pygame screen
    pygame.init()

 #This just sets the boundary for the login page size
    window_size = (800, 600)

 #This just uses an image fron image_1 file and it creates it on the login page
    screen = pygame.display.set_mode(window_size)
    # bg_image = pygame.image.load("image_1.jpg")
    # bg_image = pygame.transform.scale(bg_image, window_size)
    pygame.display.set_caption("Select level")

    icon_image = pygame.image.load("easy.jpg")
    icon_image_m = pygame.image.load("medium.jpg")
    icon_image_h = pygame.image.load("hard.jpg")

    icon_rec = icon_image.get_rec()
    icon_rec_m = icon_image_m.get_rec()
    icon_rec_h = icon_image_h.get_rec()

    icon_rec.x = 100
    icon_rec.y = 100

    icon_rec_m.x = 100
    icon_rec_m.y = 100

    icon_rec_h.x = 100
    icon_rec_h.y = 100






 #This while loop is for the keys, when the user presses a key it will do something such as writing a username and password
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSBOTTONDOWN:
                if icon_rect.collidepoint(event.pos):
                    print("the icon clicked")

        
            

        #It updates the screen
        pygame.display.flip()

        screen.blit(icon_image,icon_rec)

        pygame.display.upfdate()

    #It will freeze the screen for 3 seconds

    #Closing login screen
    pygame.quit()


    #It will return the result and username of the code
    return (result,username)


select_level()
