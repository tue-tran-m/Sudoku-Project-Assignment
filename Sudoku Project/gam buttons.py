def game_buttons(screen):
    buttonfont = pygame.font.Font(None, 40)
    # initialize text first

    resettext = buttonfont.render('RESET', 0, (255, 255, 255))
    restarttext = buttonfont.render('RESTART', 0, (255, 255, 255))
    exittext = buttonfont.render('EXIT', 0, (255, 255, 255))

    # initialize button background, color, text
    reset_surface = pygame.Surface((resettext.get_size()[0] + 20, resettext.get_size()[1] + 20))
    reset_surface.fill((20, 30, 40))
    reset_surface.blit(resettext, (10, 10))

    restart_surface = pygame.Surface((restarttext.get_size()[0] + 20, restarttext.get_size()[1] + 20))
    restart_surface.fill((20, 30, 40))
    restart_surface.blit(restarttext, (10, 10))

    exit_surface = pygame.Surface((exittext.get_size()[0] + 20, exittext.get_size()[1] + 20))
    exit_surface.fill((20, 30, 40))
    exit_surface.blit(exittext, (10, 10))

    # initialize button rectangle
    reset_rectangle = reset_surface.get_rect(center=(100, 650))
    restart_rectangle = restart_surface.get_rect(center=(300, 650))
    exit_rectangle = exit_surface.get_rect(center=(500, 650))

    # draw buttons
    screen.blit(exit_surface, exit_rectangle)
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    gamescreen = True

    while gamescreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                if reset_rectangle.collidepoint(event.pos):
                    pass
                if restart_rectangle.collidepoint(event.pos):
                    draw_game_start(screen)

        pygame.display.update()