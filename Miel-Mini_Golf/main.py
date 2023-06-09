import pygame
import os
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
HOLE_RADIUS = 20
BALL_RADIUS = 15
MODULATOR = 25

# Colors
GREEN = (24, 110, 47)
WHITE = (255, 255, 0)
BLACK = (111, 111, 111)
WATER_COLOR = (54, 84, 217)
WALL_COLOR = (111, 111, 111)
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = GREEN

# Game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Golf")
clock = pygame.time.Clock()

THEMES = [
    {
        'background': GREEN,
        'hole': WHITE,
        'ball': (255,255,0),
        'obstacle': WALL_COLOR,
        'water': WATER_COLOR,
        'text': TEXT_COLOR
    },
    {
        'background': (0, 0, 0),
        'hole': (255, 255, 255),
        'ball': (255, 255, 0),
        'obstacle': (128, 128, 128),
        'water': (0, 0, 255),
        'text': (255, 255, 255)
    },
    {
        'background': (255, 255, 255),
        'hole': (0, 0, 0),
        'ball': (0, 0, 0),
        'obstacle': (192, 192, 192),
        'water': (135, 206, 250),
        'text': (0, 0, 0)
    }
]

# Ball attributes
x = 500
y = 500
xspeed = 0
yspeed = 0

# Game state
level = 1
strokes = 0
hole_completed = False

font = pygame.font.SysFont(None, 40)

levels = {
    1: {
        'hole_position': (100, 100),
        'water_areas': [pygame.Rect(0, 200, 50, 300)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
        ]
    },
    2: {
        'hole_position': (700, 500),
        'water_areas': [pygame.Rect(200, 200, 100, 100)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(300, 300, 200, 10),  # Middle wall
        ]
    },
    3: {
        'hole_position': (400, 400),
        'water_areas': [pygame.Rect(100, 100, 200, 200)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(200, 200, 10, 200),  # Vertical wall
        ]
    },
    4: {
        'hole_position': (700, 100),
        'water_areas': [pygame.Rect(700, 300, 100, 100), pygame.Rect(800, 300, 100, 200)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(500, 100, 10, 400),  # Vertical wall 1
            pygame.Rect(600, 200, 200, 10),  # Horizontal wall
        ]
    },
    5: {
        'hole_position': (200, 500),
        'water_areas': [pygame.Rect(0, 300, 200, 200)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(100, 100, 300, 10),  # Horizontal wall
            pygame.Rect(200, 200, 10, 200),  # Vertical wall
        ]
    },
    6: {
        'hole_position': (600, 300),
        'water_areas': [pygame.Rect(400, 200, 100, 300)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(300, 100, 10, 400),  # Vertical wall
            pygame.Rect(500, 300, 200, 10),  # Horizontal wall
        ]
    },
    7: {
        'hole_position': (200, 200),
        'water_areas': [pygame.Rect(200, 100, 200, 200)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(100, 100, 10, 300),  # Vertical wall 1
            pygame.Rect(400, 200, 10, 200),  # Vertical wall 2
            pygame.Rect(200, 300, 200, 10),  # Horizontal wall
        ]
    },
    8: {
        'hole_position': (700, 200),
        'water_areas': [pygame.Rect(700, 100, 100, 100)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(500, 100, 10, 400),  # Vertical wall 1
            pygame.Rect(600, 100, 200, 10),  # Horizontal wall 1
            pygame.Rect(600, 300, 200, 10),  # Horizontal wall 2
        ]
    },
    9: {
        'hole_position': (400, 300),
        'water_areas': [pygame.Rect(100, 200, 300, 100), pygame.Rect(400, 100, 100, 200),
                        pygame.Rect(500, 300, 100, 100)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(200, 100, 300, 10),  # Horizontal wall 1
            pygame.Rect(400, 300, 100, 10),  # Horizontal wall 2
            pygame.Rect(400, 100, 10, 200),  # Vertical wall
        ]
    },
    10: {
        'hole_position': (200, 100),
        'water_areas': [pygame.Rect(0, 0, 100, 100), pygame.Rect(300, 100, 100, 100)],
        'walls': [
            pygame.Rect(0, 0, WIDTH, 10),  # Top wall
            pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),  # Right wall
            pygame.Rect(100, 100, 100, 10),  # Horizontal wall 1
            pygame.Rect(200, 200, 10, 200),  # Vertical wall
            pygame.Rect(300, 100, 10, 100),  # Vertical wall
        ]
    },
}

hit_sound = pygame.mixer.Sound("hit.mp3")
water_sound = pygame.mixer.Sound("water.mp3")
hole_sound = pygame.mixer.Sound("hole.mp3")

pygame.mixer.music.load("theme1.mp3")
pygame.mixer.music.play(-1)


def switch_theme():
    global BACKGROUND_COLOR, WHITE, BALL_COLOR, WALL_COLOR, WATER_COLOR, TEXT_COLOR
    theme = random.choice(THEMES)
    BACKGROUND_COLOR = theme['background']
    WHITE = theme['hole']
    BALL_COLOR = theme['ball']
    WALL_COLOR = theme['obstacle']
    WATER_COLOR = theme['water']
    TEXT_COLOR = theme['text']
    window.fill(BACKGROUND_COLOR)
    draw_level()


def draw_hole(position):
    pygame.draw.circle(window, WHITE, position, HOLE_RADIUS)
    pygame.draw.circle(window, BLACK, position, HOLE_RADIUS - 1)


def draw_obstacles(water_areas, walls):
    for patch in water_areas:
        pygame.draw.rect(window, WATER_COLOR, patch)

    for wall in walls:
        pygame.draw.rect(window, WALL_COLOR, wall)


def handle_collisions(water_areas, walls, hole_position):
    global xspeed, yspeed, hole_completed

    for patch in water_areas:
        if patch.collidepoint(x, y):
            reset_ball_position()
            xspeed = 0
            yspeed = 0
            water_sound.play()

    for wall in walls:
        if wall.colliderect(pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            if wall.width == WIDTH:  # Top or bottom wall
                yspeed *= -1
            else:  # Left or right wall
                xspeed *= -1

    hole = pygame.Rect(hole_position[0] - HOLE_RADIUS, hole_position[1] - HOLE_RADIUS, HOLE_RADIUS * 2, HOLE_RADIUS * 2)
    if hole.collidepoint(x, y) and abs(yspeed) < 0.1 and abs(xspeed) < 0.1:
        xspeed *= 0.97
        yspeed *= 0.97
        if not hole_completed:
            hole_completed = True
            update_score(strokes)
            display_message(f"Nice! Level {level} completed!")
            hole_sound.play()


def display_message(message):
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)


def reset_ball_position():
    global x, y
    x = 500
    y = 500


def update_score(score):
    if level in level_scores:
        level_scores[level] += score
    else:
        level_scores[level] = score


def next_level():
    global level, strokes, hole_completed
    level += 1
    strokes = 0
    hole_completed = False
    reset_ball_position()


def draw_level():
    window.fill(BACKGROUND_COLOR)

    hole_position = levels[level]['hole_position']
    water_areas = levels[level]['water_areas']
    walls = levels[level]['walls']

    for patch in water_areas:
        pygame.draw.rect(window, WATER_COLOR, patch)

    for wall in walls:
        pygame.draw.rect(window, WALL_COLOR, wall)

    draw_hole(hole_position)
    pygame.draw.circle(window, WHITE, (round(x), round(y)), BALL_RADIUS)


level_scores = {}  # Dictionary to store scores for each level

running = True
while running:
    window.fill(BACKGROUND_COLOR)

    hole_position = levels[level]['hole_position']
    water_areas = levels[level]['water_areas']
    walls = levels[level]['walls']

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and not hole_completed:
            pos = pygame.mouse.get_pos()
            xspeed = (pos[0] - x) // MODULATOR
            yspeed = (pos[1] - y) // MODULATOR
            strokes += 1
            hit_sound.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_ball_position()
                xspeed = 0
                yspeed = 0
                hole_completed = False
                strokes = 0
            elif event.key == pygame.K_n:
                if hole_completed:
                    next_level()
            elif event.key == pygame.K_t:
                switch_theme()  # Handle theme switching event
                pygame.display.update()

    if not hole_completed:
        x += xspeed
        y += yspeed
        xspeed *= 0.98
        yspeed *= 0.98

        if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
            pygame.draw.line(window, (255, 165, 0), (x, y), pygame.mouse.get_pos())

        handle_collisions(water_areas, walls, hole_position)
        draw_hole(hole_position)
        draw_obstacles(water_areas, walls)
        pygame.draw.circle(window, WHITE, (round(x), round(y)), BALL_RADIUS)
    else:
        display_message("Press R to restart or N for next level")

    # Display level and score
    level_text = font.render(f"Level: {level}", True, TEXT_COLOR)
    level_rect = level_text.get_rect(topright=(WIDTH - 20, 20))
    window.blit(level_text, level_rect)

    score_text = font.render(f"Score: {level_scores.get(level, 0)}", True, TEXT_COLOR)
    score_rect = score_text.get_rect(topright=(WIDTH - 20, 60))
    window.blit(score_text, score_rect)

    button_text = font.render("Switch Theme (T)", True, TEXT_COLOR)
    button_rect = button_text.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
    pygame.draw.rect(window, WHITE, button_rect, 2)
    window.blit(button_text, button_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
