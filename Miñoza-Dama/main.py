import pygame
import pygame.mixer
import pygame.font
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

pygame.mixer.init()
move_sound = pygame.mixer.Sound('C:/Users/rubom/PycharmProjects/DamaProject/click.wav')  # Replace 'move_sound.wav' with the actual file name and extension
pygame.font.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    winner_message = None
    congrats_message = None

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                move_sound.play()

        game.update()

    if winner_message:
        WIN.blit(winner_message, ((WIDTH - winner_message.get_width()) // 2, (HEIGHT - winner_message.get_height()) // 2))
        pygame.display.update()

    if congrats_message:
        WIN.blit(congrats_message, ((WIDTH - congrats_message.get_width()) // 2, (HEIGHT - congrats_message.get_height()) // 2 - 60))
        pygame.display.update()

    pygame.quit()


main()
