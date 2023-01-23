import pygame
import time
import os

def sign_up_user():


    pygame.init()

    window_size = (600, 400)

 #This just uses an image fron image_1 file and it creates it on the login page
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Sign-up page!")

 #This just sets the default font for all the texts 
    font = pygame.font.Font(None, 32)

 #We are going to check username and password and check to see if its correct in the data.text
    data = {}
    with open ("data.txt") as f:
        for line in f:
        
            (key, val) = line.split(",")
            data[key] = val[:-1]
    
    message = " "

    username = ""
    password = ""
    #print(data)
 #Determines the font color on the username and passwords 
    username_label = font.render("New User: ", True, (255, 255, 255))
    password_label = font.render("Password: ", True, (255, 255, 255))

 #Puts an image on the login page
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
                    data_temp = open("data_temp.txt", "a")
                    data[username] = password
                    new_user_result = username


                    for u in data:
                        data_temp.write(u + ',' + str(data[u])+'\n')

                    data_temp.write('---,---')
                    f.close()
                    data_temp.close()
                    os.remove("data.txt")
                    os.rename("data_temp.txt","data.txt")


                    message_1 = font.render("Sign-up successfully!", True,(0, 255, 0))
                    screen.blit(message_1, (50, 250))
                        
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
    return new_user_result
    #print(data)

# sign_up_user()
