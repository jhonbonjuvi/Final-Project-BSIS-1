import pygame
from pygame.locals import *
import random

pygame.init()

# create the window
width = 500
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

# colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# road and marker sizes
road_width = 300
marker_width = 10
marker_height = 50

# lane coordinates
left_lane = 150
center_lane = 250
right_lane = 350
top_lane = 50
bottom_lane = 450
lanes = [left_lane, center_lane, right_lane]

# road and edge markers
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# for animating movement of the lane markers
lane_marker_move_y = 0

# player's starting coordinates
player_x = 250
player_y = 400

# frame settings
clock = pygame.time.Clock()
fps = 120

pygame.mixer.music.load("C:/Users/rubom/PycharmProjects/Car_Games/sound.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class Vehicle(pygame.sprite.Sprite):

    def __init__(self, images, x, a):
        pygame.sprite.Sprite.__init__(self)

        image_scale = 45 / images.get_rect().width
        new_width = images.get_rect().width * image_scale
        new_height = images.get_rect().height * image_scale
        self.image = pygame.transform.scale(images, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, a]


class PlayerVehicle(Vehicle):
    def __init__(self, x, a):
        image1 = pygame.image.load('C:/Users/rubom/PycharmProjects/Car_Games/image2.png')
        super().__init__(image1, x, a)


# sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# create the player's car
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# load the vehicle images
image_filenames = ['C:/Users/rubom/PycharmProjects/Car_Games/pickup_truck.png', 'C:/Users/rubom/PycharmProjects/Car_Games/semi_trailer.png', 'C:/Users/rubom/PycharmProjects/Car_Games/taxi.png', 'C:/Users/rubom/PycharmProjects/Car_Games/van.png', 'C:/Users/rubom/PycharmProjects/Car_Games/car.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load(image_filename)
    vehicle_images.append(image)

# load the crash image
crash = pygame.image.load('C:/Users/rubom/PycharmProjects/Car_Games/crash.png')
crash_rect = crash.get_rect()

# high score
gameover = False
speed = 2
score = 0

# high score
high_score = 0


# load the high score
# load the high score
def load_high_score():
    try:
        with open("C:/Users/rubom/PycharmProjects/Car_Games/highscore.txt", "r") as file:
            high_score_str = file.read()
            if high_score_str:
                return int(high_score_str)
            else:
                return 0
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


# save the high score
def save_high_score():
    with open("C:/Users/rubom/PycharmProjects/Car_Games/highscore.txt", "w") as file:
        file.write(str(high_score))


# update the high score
def update_high_score():
    global high_score
    if score > high_score:
        high_score = score
        save_high_score()


# game loop
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # move the player's car using the left/right arrow keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 50
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 50
            elif event.key == K_UP and player.rect.centery > top_lane:
                player.rect.y -= 100
            elif event.key == K_DOWN and player.rect.centery < bottom_lane:
                player.rect.y += 100

            # check if there's a sideswipe collision after changing lanes
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):

                    gameover = True

                    # place the player's car next to other vehicle
                    # and determine where to position the crash image
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

    screen.fill(green)

    # draw the road
    pygame.draw.rect(screen, gray, road)

    # draw the edge markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # draw the lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    # draw the player's car
    player_group.draw(screen)

    # add a vehicle
    if len(vehicle_group) < 2:

        # ensure there's enough gap between vehicles
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False

        if add_vehicle:
            # select a random lane
            lane = random.choice(lanes)

            # select a random vehicle image
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    # make the vehicles move
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()

            # add to score
            score += 1

            # speed up the game after passing 5 vehicles
            if score > 0 and score % 5 == 0:
                speed += 1

    # draw the vehicles
    vehicle_group.draw(screen)

    # display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    score_text = font.render('Score: ' + str(score), True, red)
    text_rect = score_text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(score_text, text_rect)

    # check if there's a head-on collision
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
        crash_sound = pygame.mixer.Sound("C:/Users/rubom/PycharmProjects/Car_Games/crash1.wav")
        crash_sound.set_volume(0.8)
        crash_sound.play()

    if gameover:
        screen.blit(crash, crash_rect)
        pygame.mixer.music.stop()

        # display the game over text
        font = pygame.font.Font(pygame.font.get_default_font(), 70)
        text = font.render('Game Over', True, red)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2)
        screen.blit(text, text_rect)

        # display the high score
        high_score = load_high_score()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        text = font.render('High Score: ' + str(high_score), True, red)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2 + 100)
        screen.blit(text, text_rect)

        # update and display the high score
        update_high_score()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        text = font.render('New High Score: ' + str(high_score), True, red)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2 + 250)
        screen.blit(text, text_rect)

        # reset the game
        pygame.display.flip()
        pygame.time.wait(2000)
        gameover = False
        score = 0
        speed = 2
        player.rect.x = player_x
        player.rect.y = player_y
        vehicle_group.empty()
        pygame.mixer.music.play(-1)

    pygame.display.flip()

pygame.quit()
