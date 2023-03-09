import pygame
from string import ascii_letters
from random import choice

def check_line(line, line_number):
    colours = []
    for i in range(5):
        colours.append(GREY)
    for p in range (5):
        if line[line_number][p] == word[p]:
            colours[p] = GREEN
            letters[p] = None
    for q in range (5):
        for i in range(5):
            if colours[q] != GREEN:
                if line[line_number][q] == letters[i]:
                    letters[i] = None
                    colours[q] = YELLOW
    complete = True
    for each in colours:
        if each != GREEN:
            complete = False
    return colours, complete

def empty_lines():
    return [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

def get_new_word():
    f = open('text.txt', 'r')
    file = f.read().splitlines()
    f.close()
    word = choice(file)
    return word

def check_word(word):
    f = open('accepted.txt', 'r')
    file = f.read().splitlines()
    f.close()
    for each in file:
        if word == each:
            return True
    return False

############################################################################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 215, 0)
YELLOW = (255, 215, 0)

good_char = ascii_letters
word = get_new_word()
lines = empty_lines()

line_number = 0
end = False
error = False
user_input = ''

letters = []
background = []
for each_letter in word:
    letters.append(each_letter)

pygame.init()
screen = pygame.display.set_mode((440, 550))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if pygame.mouse.get_pressed()[0]:
            if new_game_rect.collidepoint(pygame.mouse.get_pos()):
                lines = empty_lines()
                end = False
                line_number = 0
                word = get_new_word()
                background = []
                letters = []
                for each_letter in word:
                    letters.append(each_letter)
        if end != True:
            if event.type == pygame.KEYDOWN:
                temp = []
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                if len(user_input) < 5:
                    for each in good_char:
                        if event.unicode == each:
                            user_input += (event.unicode).upper()
                            break
                for each in user_input:
                    temp.append(each)   
                for x in range(len(word) - len(temp)):
                    temp.append(' ')
                lines[line_number] = temp
                if event.key == pygame.K_RETURN and len(user_input) == 5 and not(check_word(user_input)):
                    error = True
                if event.key == pygame.K_RETURN and len(user_input) == 5 and check_word(user_input):
                    error = False
                    for i in range(len(user_input)):
                        lines[line_number][i] = user_input[i]
                    colour = check_line(lines, line_number)
                    background.append(colour[0])
                    line_number += 1
                    if line_number == 6 or colour[1]:
                        end = True
                    next_row = True
                    user_input = ''
                    letters = []
                    for each_letter in word:
                        letters.append(each_letter)
# drawing the empty squares
    y = 60
    for q in range(1, 7):
        x = 60
        for p in range(1, len(word) + 1):
            pygame.draw.rect(screen, BLACK, (x, y, 60, 60))
            pygame.draw.rect(screen, GREY, (x, y, 60, 60), 2)
            if len(background) >= q:
                pygame.draw.rect(screen, background[q - 1][p - 1], (x, y, 60, 60))
            x += 65
        y += 65 
# drawing the letters in the squares
    y = 60
    for q in range(1, len(lines) + 1):
        x = 60
        for p in range(1, len(lines[q - 1]) + 1):
            font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Wordle\Arial.ttf", 50)
            text_surf = font.render(lines[q - 1][p - 1], True, WHITE)
            text_rect = text_surf.get_rect(center = (x + 30, y + 30))
            screen.blit(text_surf, text_rect)
            x += 65
        y += 65 
    pygame.draw.rect(screen, BLACK, (0, 450, 440, 55))
    font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Wordle\Arial.ttf", 30)
    if end:
        if colour[1]:
            text = f'Solved in {line_number} tries'
        else:
            text = f'Answer: {word}'
        text_surf = font.render(text, False, WHITE)
        text_rect = text_surf.get_rect(center = (220, 475))
        screen.blit(text_surf, text_rect)
    if error:
        text = 'Not a vaild word!'
        text_surf = font.render(text, False, WHITE)
        text_rect = text_surf.get_rect(center = (220, 475))
        screen.blit(text_surf, text_rect)
# drawing out the back button
    font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Wordle\Arial.ttf", 20)
    new_game_text_surf = font.render('New game', True, BLACK)
    new_game_text_rect = new_game_text_surf.get_rect(center = (220, 525))
    new_game_rect = pygame.Rect((145, 500, 150, 50))
    pygame.draw.rect(screen, YELLOW, new_game_rect)
    pygame.draw.rect(screen, WHITE, new_game_rect, 2)
    screen.blit(new_game_text_surf, new_game_text_rect)    
    pygame.display.update()
    clock.tick(60)