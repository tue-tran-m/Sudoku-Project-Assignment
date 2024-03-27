import pygame
from constants import *
import sys

def win():
    screen.fill(BG_COLOR)
    win_font = pygame.font.Font(None, 150)
    win_surface = win_font.render('Game Won!:)', 0, CHIP_FONT)
    win_rectangle = win_surface.get_rect(center = (WIDTH//2, 250))
    screen.blit(win_surface, win_rectangle)

    #exit button
    button_font = pygame.font.Font(None, 70)
    exit_text = button_font.render("Exit", 0, BG_COLOR)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def lose():
    screen.fill(BG_COLOR)
    lose_font = pygame.font.Font(None, 150)
    lose_surface = lose_font.render('Game Over:(', 0, CHIP_FONT)
    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, 250))
    screen.blit(lose_surface, lose_rectangle)

    #restart button
    button_font = pygame.font.Font(None, 70)
    restart_text = button_font.render("Exit", 0, BG_COLOR)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    pass


   

