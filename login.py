# login module



#What the import time does it takes 3 seconds after when you login with your username and password to open up a new page 
import time
#Import pygame is just imports all the avaible pygame modules
import pygame


#def is to define a function 
def login_pygame():
    result = False

 #initializes the pygame screen
    pygame.init()

 #This just sets the boundary for the login page size
    window_size = (600, 400)

 #This just uses an image fron image_1 file and it creates it on the login page
    screen = pygame.display.set_mode(window_size)
    bg_image = pygame.image.load("image_1.jpg")
    bg_image = pygame.transform.scale(bg_image, window_size)
    pygame.display.set_caption("User name and Password")

 #This just sets the default font for all the texts 
    font = pygame.font.Font(None, 32)

 #We are going to check username and password and check to see if its correcy in the data.text
    data = {}
    with open ("data.txt") as f:
        for line in f:
        
            (key, val) = line.split(",")
            data[key] = val[:-1]
    
    message = " "

    username = ""
    password = ""

 #Determines the font color on the username and passwords 
    username_label = font.render("User Name: ", True, (255, 255, 255))
    password_label = font.render("Password: ", True, (255, 255, 255))

 #Puts an image on the login page
    screen.blit(bg_image,(0,0))
    screen.blit(username_label, (50, 50))
    screen.blit(password_label, (50, 100))
 
 #It will create a rectangle with the sizes of it
    username_rect = pygame.Rect(200, 50, 200, 32)
    password_rect = pygame.Rect(200, 100, 200, 32)

    pygame.draw.rect(screen, (255, 255, 255), username_rect)
    pygame.draw.rect(screen, (255, 255, 255), password_rect)

 #This means that when the page loads, the user can start clicking and writing
    active_input_field = "username"
    running = True

 #This while loop is for the keys, when the user presses a key it will do something such as writing a username and password
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if active_input_field == "username":
                        username = username[:-1]
                    if active_input_field == "password":
                        password = password[:-1]
                elif event.key == pygame.K_TAB:
                    if active_input_field == "username":
                        active_input_field = "password"
                    elif active_input_field == "password":
                        active_input_field = "username"


                #This is for if their is an correct username 
                elif event.key == pygame.K_RETURN:
                    if username in data.keys() and data[username] == password:
                        message_1 = font.render("Login successful", True,
                                            (0, 255, 0))
                        message_2 = font.render("Now let's go to text based game!", True,
                                            (0, 255, 0))
                        screen.blit(message_1, (50, 250))
                        screen.blit(message_2, (50,300))
                        running = False
                        result = True

                        #This is for an incorrect/invalid username or password
                    else:
                        message = font.render("Invalid user name or password",
                                            True, (255, 0, 0))
                        screen.blit(message, (50, 300))
                        running = False

                #This for adding the username and password immediately to the bos that we created
                else:
                    if active_input_field == "username":
                        username += event.unicode
                    if active_input_field == "password":
                        password += event.unicode

                    
                    #This just diplays what font and color will the text of the username and password will be
                    username_text = font.render(username, True, (0, 0, 0))
                    password_hidden = len(password)*"*"
                    password_text = font.render(password_hidden, True, (0, 0, 0))


                    #Saves it to username_text and password_text and it will display it
                    screen.blit(username_text, (200, 50))
                    screen.blit(password_text, (200, 100))


        #It updates the screen
        pygame.display.flip()

    #It will freeze the screen for 3 seconds
    time.sleep(3)

    #Closing login screen
    pygame.quit()


    #It will return the result and username of the code
    return (result,username)
