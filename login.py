# login module
import time


def login_page():
    log = """
          *******************************************************
          -----------------Wellcome to ----------------------\n
          -----------------HANGMAN GAME  -------------------\n
          ------------------by Hassan  -------------------------\n
          *******************************************************
        """
    print(log)
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    result = False

    data = {"testuser": "testpass"}
    if username in data.keys():
      if data[username] == password:
        print("Access granted! Login successfull!")
        result = True
    else:
        print("Access denied! Username or Password is not correct!")

    return result

def login_pygame():
    result = False

    import pygame

    pygame.init()

    window_size = (600, 400)

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("User name and Password")

    font = pygame.font.Font(None, 32)

    data = {}
    with open ("data.txt") as f:
        for line in f:
        #print(line)
            (key, val) = line.split(",")
            data[key] = val[:-1]
    #print(data)
    
    #data = {"testuser": "testpass", "test":"test"}
    #correct_username = "test"
    #correct_password = "test"
    message = " "

    username = ""
    password = ""

    username_label = font.render("User Name: ", True, (255, 255, 255))
    password_label = font.render("Password: ", True, (255, 255, 255))

    screen.blit(username_label, (50, 50))
    screen.blit(password_label, (50, 100))

    username_rect = pygame.Rect(200, 50, 200, 32)
    password_rect = pygame.Rect(200, 100, 200, 32)

    pygame.draw.rect(screen, (255, 255, 255), username_rect)
    pygame.draw.rect(screen, (255, 255, 255), password_rect)

    active_input_field = "username"
    running = True
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
                elif event.key == pygame.K_RETURN:
                    if username in data.keys() and data[username] == password:
                    #if username == correct_username and password == correct_password:
                        message = font.render("Login successful", True,
                                            (0, 255, 0))
                        message = font.render("Now let's go to text based game!", True,
                                            (0, 255, 0))
                        screen.blit(message, (50, 150))
                        running = False
                        result = True
                    else:
                        message = font.render("Invalid user name or password",
                                            True, (255, 0, 0))
                        screen.blit(message, (50, 150))
                        running = False

                else:
                    if active_input_field == "username":
                        username += event.unicode
                    if active_input_field == "password":
                        password += event.unicode

                    username_text = font.render(username, True, (0, 0, 0))
                    password_hidden = len(password)*"*"
                    password_text = font.render(password_hidden, True, (0, 0, 0))

                    screen.blit(username_text, (200, 50))
                    screen.blit(password_text, (200, 100))

        pygame.display.flip()

    time.sleep(3)
    pygame.quit()

    return (result,username)
