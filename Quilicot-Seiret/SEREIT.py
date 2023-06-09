import pygame
from pygame.locals import *
import random
import sys


pygame.init()

# Set up the display window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SEREIT")

clock = pygame.time.Clock()

# List of words to choose from
word_list = ["SEREIT", "PYTHON", "GAMING", "OPENAI", "COMPUTER, PROGRAMMING"]
chosen_word = random.choice(word_list)

# Game variables
word = "_" * len(chosen_word)
guessed_letters = []
mistakes = 0



# Hangman figure
hangman_images = [
   pygame.image.load("white.png"),
    pygame.image.load("s.png"),
    pygame.image.load("se.png"),
    pygame.image.load("ser.png"),
    pygame.image.load("sere.png"),
    pygame.image.load("serei.png"),
    pygame.image.load("seiret.png"),
    pygame.image.load("seiret.png"),
]

# Game state
game_over = False
game_result = ""


# Button dimensions and colors
button_width, button_height = 120, 50
button_color = (0, 100, 200)
button_hover_color = (0, 150, 255)

# Quit button
quit_button_x, quit_button_y = window_width // 2 - button_width // 2, window_height - button_height - 50
quit_button_rect = pygame.Rect(quit_button_x, quit_button_y, button_width, button_height)

# Play again button
play_again_button_x, play_again_button_y = window_width // 2 - button_width // 2, window_height // 2
play_again_button_rect = pygame.Rect(play_again_button_x, play_again_button_y, button_width, button_height)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            

        # Keyboard events
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                

            if game_over:
                # Restart the game when any key is pressed after game over
                chosen_word = random.choice(word_list)
                word = "_" * len(chosen_word)
                guessed_letters = []
                mistakes = 0
                game_over = False
                game_result = ""


            # Check if the pressed key is a letter and hasn't been guessed before
            if event.key in range(K_a, K_z + 1) and not game_over:
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.append(letter)
                    if letter not in chosen_word:
                        mistakes += 1
                    else:
                        # Update the word with the correctly guessed letter
                        updated_word = ""
                        for i, char in enumerate(chosen_word):
                            if char == letter:
                                updated_word += char
                            else:
                                updated_word += word[i]
                        word = updated_word

        # Mouse events
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                letter_clicked = None

                if game_over:
                    # Restart the game when left mouse button is clicked after game over
                    chosen_word = random.choice(word_list)
                    word = "_" * len(chosen_word)
                    guessed_letters = []
                    mistakes = 0
                    game_over = False
                    game_result = ""
                    
                # Check if the quit button was clicked
                if quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

                else:
                    # Check if a letter button was clicked
                    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        letter_x = 50 + (i % 13) * 50
                        letter_y = 400 + (i // 13) * 50
                        letter_rect = pygame.Rect(letter_x, letter_y, 40, 40)
                        if letter_rect.collidepoint(mouse_pos):
                            letter_clicked = letter
                            break

                    if letter_clicked and letter_clicked not in guessed_letters:
                        guessed_letters.append(letter_clicked)
                        if letter_clicked not in chosen_word:
                            mistakes += 1
                        else:
                            # Update the word with the correctly guessed letter
                            updated_word = ""
                            for i, char in enumerate(chosen_word):
                                if char == letter_clicked:
                                    updated_word += char
                                else:
                                    updated_word += word[i]
                            word = updated_word

    # Clear the display
    window.fill((255, 255, 255))

    if not game_over:
        # Draw the hangman figure
        window.blit(hangman_images[mistakes], (100, 50))

        # Draw the word and guessed letters
        font = pygame.font.Font(None, 48)
        word_text = font.render(word, True, (0, 0, 0))
        window.blit(word_text, (50, 300))

        # Draw the letter buttons
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            letter_x = 50 + (i % 13) * 50
            letter_y = 400 + (i // 13) * 50
            letter_rect = pygame.Rect(letter_x, letter_y, 40, 40)

            button_color = (255, 255, 255) if letter in guessed_letters else (255, 0, 0)
            pygame.draw.rect(window, button_color, letter_rect)

            letter_text = font.render(letter, True, (255, 255, 255))
            letter_text_rect = letter_text.get_rect(center=letter_rect.center)
            window.blit(letter_text, letter_text_rect)
    else:
        # Draw game over message
        font = pygame.font.Font(None, 30)
        game_over_text = font.render(game_result, True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(game_over_text, game_over_text_rect)

        # Draw the quit button
        pygame.draw.rect(window, button_color, quit_button_rect)
        quit_text = font.render("Quit", True, (0, 0, 0))
        quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
        window.blit(quit_text, quit_text_rect)
    

        # Draw the play again button
        pygame.draw.rect(window, button_color, play_again_button_rect)
        play_again_text = font.render("Play Again", True, (0, 0, 0))
        play_again_text_rect = play_again_text.get_rect(center=play_again_button_rect.center)
        window.blit(play_again_text, play_again_text_rect)


    # Check game result
    if mistakes >= len(hangman_images) - 1:
        game_over = True
    elif "_" not in word:
        game_over = True
    

    pygame.display.update()
    clock.tick(60)
