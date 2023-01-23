import pygame #This Imports all the avaible pygame modules

#This is for selecting the level 
def select_level():

    #This is for if running a loop without breaking 
    running = True
    selected_level = "easy"

    

    #initializes the pygame screen
    pygame.init()

    #Uses the font for everthing 
    font = pygame.font.Font(None, 32)

    #This just sets the boundary for the login page size
    window_size = (800, 600)
    icon_size = (100,150)

    #This is for to display the window size
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Select level")

    #This for scaling the icon images 
    icon_image_e_0 = pygame.image.load("Easy.jpg")
    icon_image_e = pygame.transform.scale(icon_image_e_0, icon_size)
    icon_image_m_0 = pygame.image.load("medium.jpg")
    icon_image_m = pygame.transform.scale(icon_image_m_0, icon_size)
    icon_image_h_0 = pygame.image.load("hard.jpg")
    icon_image_h = pygame.transform.scale(icon_image_h_0, icon_size)

    #This for the font used for which level do you want 
    select_level_label = font.render("Which level do you choose? (easy/medium/hard):", True, (255, 255, 255))

    #This is for positioning 
    screen.blit(select_level_label, (100, 100))
    

    #This changes the icon images to rectangles
    icon_rec_e = icon_image_e.get_rect()
    icon_rec_m = icon_image_m.get_rect()
    icon_rec_h = icon_image_h.get_rect()

    #This is for positioning of each icon image
    icon_rec_e.x = 200
    icon_rec_e.y = 200

    icon_rec_m.x = 400
    icon_rec_m.y = 200

    icon_rec_h.x = 600
    icon_rec_h.y = 200

    #This is for exiting the screen 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #This is for if the user is clicking on an icon, it will select that level for my game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if icon_rec_e.collidepoint(event.pos):
                    selected_level = "easy"
                    running = False
                elif icon_rec_m.collidepoint(event.pos):
                    selected_level = "medium"
                    running = False
                elif icon_rec_h.collidepoint(event.pos):
                    selected_level = "githard"
                    running = False

        
            

        #It updates the screen
        pygame.display.flip()

        #This displays the icon images on the screen 
        screen.blit(icon_image_e,icon_rec_e)
        screen.blit(icon_image_m,icon_rec_m)
        screen.blit(icon_image_h,icon_rec_h)

        #Updates the screen
        pygame.display.update()

    #Quits the screen if user clicks red button
    pygame.quit()

    #Return the level when the user clicked it and it will transfer it to the main game
    return selected_level


