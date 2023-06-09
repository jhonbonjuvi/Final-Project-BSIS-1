import pygame
from math import pi, cos, sin
import datetime

# Screen dimensions
WIDTH, HEIGHT = 500, 700

# Clock parameters
clock_radius = 200
center = (WIDTH // 2, HEIGHT // 2)

# Colors
LIGHT_MODE = {
    "background": (255, 255, 255),
    "clock_face": (0, 0, 0),
    "hour_hand": (0, 0, 0),
    "minute_hand": (0, 0, 0),
    "second_hand": (255, 0, 0),
    "marker": (0, 0, 0),
    "text": (0, 0, 0),
}

DARK_MODE = {
    "background": (0, 0, 0),
    "clock_face": (255, 255, 255),
    "hour_hand": (255, 255, 255),
    "minute_hand": (255, 255, 255),
    "second_hand": (255, 0, 0),
    "marker": (255, 255, 255),
    "text": (255, 255, 255),
}

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load button click sound effect
button_click_sound = pygame.mixer.Sound("C:/Users/ACER/PycharmProjects/pythonProject5/click.wav")

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog and Digital Clock")

# Clock settings
clock = pygame.time.Clock()
FPS = 60


# Helper function to render and display text on the screen
def render_text(text, size, position, color):
    font = pygame.font.SysFont("times new roman", size, True, False)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)


# Helper function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(radius, theta):
    x = radius * sin(pi * theta / 180)
    y = radius * cos(pi * theta / 180)
    return center[0] + x, center[1] - y


# Render and display the digital clock
def render_digital_clock(current_time, color):
    time_str = current_time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM indicator
    render_text(time_str, 30, (center[0], HEIGHT // 8), color)


# Render and display the date
def render_date(current_time, color):
    month_str = current_time.strftime("%B")  # Full month name
    day_str = current_time.strftime("%d")  # Day of the month
    year_str = current_time.strftime("%Y")  # Full year
    date_str = f"{month_str} {day_str}, {year_str}"
    render_text(date_str, 30, (center[0], center[1] + clock_radius + 50), color)


# Helper function to handle button clicks
def handle_button_click(mouse_pos, button_rect, dark_mode):
    if button_rect.collidepoint(mouse_pos):
        dark_mode = not dark_mode
        button_click_sound.play()  # Play the button click sound effect
    return dark_mode


# Main function
def main():
    run = True
    dark_mode = False
    color_scheme = LIGHT_MODE

    # Button parameters
    button_size = (100, 30)
    button_pos = (WIDTH - button_size[0] - 20, 20)
    button_rect = pygame.Rect(button_pos, button_size)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                dark_mode = handle_button_click(mouse_pos, button_rect, dark_mode)

        # Get the current time
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        # Clear the screen
        screen.fill(color_scheme["background"])

        # Draw clock face
        pygame.draw.circle(screen, color_scheme["clock_face"], center, clock_radius - 10, 10)
        pygame.draw.circle(screen, color_scheme["clock_face"], center, 12)

        # Draw hour markers
        for number in range(1, 13):
            marker_pos = polar_to_cartesian(clock_radius - 50, number * 30)
            render_text(str(number), 30, marker_pos, color_scheme["marker"])

        # Draw minute markers
        for number in range(0, 360, 6):
            marker_start = polar_to_cartesian(clock_radius - 15, number)
            marker_end = polar_to_cartesian(clock_radius - 30, number) if number % 5 else polar_to_cartesian(
                clock_radius - 35, number)
            pygame.draw.line(screen, color_scheme["marker"], marker_start, marker_end, 2)

        # Draw hour hand
        hour_hand_length = clock_radius - 100
        hour_angle = (hour + minute / 60 + second / 3600) * (360 / 12)
        hour_hand_end = polar_to_cartesian(hour_hand_length, hour_angle)
        pygame.draw.line(screen, color_scheme["hour_hand"], center, hour_hand_end, 10)

        # Draw minute hand
        minute_hand_length = clock_radius - 70
        minute_angle = (minute + second / 60) * (360 / 60)
        minute_hand_end = polar_to_cartesian(minute_hand_length, minute_angle)
        pygame.draw.line(screen, color_scheme["minute_hand"], center, minute_hand_end, 6)

        # Draw second hand
        second_hand_length = clock_radius - 60
        second_angle = second * (360 / 60)
        second_hand_end = polar_to_cartesian(second_hand_length, second_angle)
        pygame.draw.line(screen, color_scheme["second_hand"], center, second_hand_end, 2)

        # Draw digital clock
        render_digital_clock(current_time, color_scheme["text"])

        # Draw date
        render_date(current_time, color_scheme["text"])

        # Draw dark mode button
        button_text = "Light Mode" if dark_mode else "Dark Mode"
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        render_text(button_text, 20, (button_pos[0] + button_size[0] // 2, button_pos[1] + button_size[1] // 2),
                    (255, 255, 255))

        # Toggle color scheme
        if dark_mode:
            color_scheme = DARK_MODE
        else:
            color_scheme = LIGHT_MODE

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FPS)

    # Quit the program
    pygame.quit()


# Run the main function
if __name__ == "__main__":
    main()
