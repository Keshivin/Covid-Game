# import modules
import pygame
import random

# initialize pygame
pygame.init()

# Here I set game window
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Images in this program are downloaded from freepik.com and flaticon.com

# Here I define the background variable
background = pygame.image.load("backed.jpg")

# Here I set caption and icon
pygame.display.set_caption("Covid")
icon = pygame.image.load("coverall.png")
pygame.display.set_icon(icon)

# Here I set the Player and the position for the Player
player = pygame.image.load("malee.png")
player_width = player.get_width()
player_height = player.get_height()
player_x_position = 450
player_y_position = 500

# Here I set the Prize and the position for the Prize
prize = pygame.image.load("vaccine.png")
prize_width = prize.get_width()
prize_height = prize.get_height()
prize_X_Position = 400
prize_Y_Position = 0 - prize_height


# Here I set enemy1 and the position of the enemy1
enemy1 = pygame.image.load("virus.png")
enemy1_width = enemy1.get_width()
enemy1_height = enemy1.get_height()
enemy1_X_Position = random.randint(0, screen_width - 30)
enemy1_Y_Position = 0 - enemy1_height

# Here I set enemy2 and the position of the enemy2
enemy2 = pygame.image.load("coronavirus.png")
enemy2_width = enemy2.get_width()
enemy2_height = enemy2.get_height()
enemy2_X_Position = random.randint(0, screen_width - 30)
enemy2_Y_Position = 0 - enemy2_height

# Here I set enemy3 and the position of the enemy3
enemy3 = pygame.image.load("bacteria.png")
enemy3_width = enemy3.get_width()
enemy3_height = enemy3.get_height()
enemy3_X_Position = random.randint(0, screen_width - 30)
enemy3_Y_Position = 0 - enemy3_height

# Here I set the speed of game icons
speed = 1
enemy_speed = 0.5
prize_speed = 0.3

# Here is the Main While game loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # here I check if any keys are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x_position -= speed

    elif keys[pygame.K_RIGHT]:
        player_x_position += speed

    elif keys[pygame.K_DOWN]:
        player_y_position += speed

    elif keys[pygame.K_UP]:
        player_y_position -= speed

    # Here I set the boundaries

    # This is player_x_position

    # left side
    if player_x_position <= 0:
        player_x_position = 0

    # right side
    elif player_x_position >= screen_width - player_width:
        player_x_position = screen_width - player_width

    # This is player_y_position

    # top
    if player_y_position <= 0:
        player_y_position = 0

    # bottom
    elif player_y_position >= screen_height - player_height:
        player_y_position = screen_height - player_height

    # set the fill screen to create movement even when the object is incremented
    screen.fill((0, 0, 0))

    # set the background
    screen.blit(background, (0, 0))

    # Here we draw the player
    screen.blit(player, (player_x_position, player_y_position, player_width, player_height))

    # Create a Bounding box for the player:
    player_box = pygame.Rect(player.get_rect())

    # update the box position to player position
    player_box.top = player_y_position - 10
    player_box.left = player_x_position - 10

    # display enemies and map movements
    # enemy1
    screen.blit(enemy1, (enemy1_X_Position, enemy1_Y_Position, enemy1_width, enemy1_height))
    enemy1_Y_Position += enemy_speed

    # Bounding box for enemy1:
    enemy1_box = pygame.Rect(enemy1.get_rect())

    # update box position to enemy1 position
    enemy1_box.top = enemy1_Y_Position - 30
    enemy1_box.left = enemy1_X_Position - 30

    # enemy2
    if enemy1_Y_Position >= screen_height:
        screen.blit(enemy2, (enemy2_X_Position, enemy2_Y_Position, enemy2_width, enemy2_height))
        enemy2_Y_Position += enemy_speed

    # Bounding box for enemy2
    enemy2_box = pygame.Rect(enemy2.get_rect())

    # update box position to enemy2 position
    enemy2_box.top = enemy2_Y_Position - 30
    enemy2_box.left = enemy2_X_Position - 30

    # enemy3
    if enemy2_Y_Position >= screen_height:
        screen.blit(enemy3, (enemy3_X_Position, enemy3_Y_Position, enemy3_width, enemy3_height))
        enemy3_Y_Position += enemy_speed

    # Bounding box for enemy3
    enemy3_box = pygame.Rect(enemy3.get_rect())

    # update box position to enemy3 position
    enemy3_box.top = enemy3_Y_Position - 30
    enemy3_box.left = enemy3_X_Position - 30

    # prize
    # display the prize if 3rd enemy has left window and map movements
    if enemy3_Y_Position >= screen_height:
        screen.blit(prize, (prize_X_Position, prize_Y_Position, prize_width, prize_height))
        prize_Y_Position += prize_speed

    # if prize leaves window make it appear again
    if prize_Y_Position >= screen_height:
        prize_Y_Position = 0 - prize_height
        prize_Y_Position += prize_speed

    # create a bounding box for prize
    prize_box = pygame.Rect(prize.get_rect())

    # update the box position to prize position
    prize_box.top = prize_Y_Position - 30
    prize_box.left = prize_X_Position - 30

    # Test the collision of the boxes:
    if player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box):
        # Display losing status to the user:
        print("You lose!")

        # quit game and exit window:
        pygame.quit()
        exit(0)

    if player_box.colliderect(prize_box):
        # display wining status to the user:
        print("You win!")

        # quit game and exit window:
        pygame.quit()

        exit(0)

    # update screen
    pygame.display.update()
