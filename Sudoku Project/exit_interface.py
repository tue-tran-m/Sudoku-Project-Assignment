def draw_game_over(screen):
    win = 9
    game_over_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 40)

    # Color background
    imp = pygame.image.load(
        "/Users/mt/Downloads/a-close-up-shot-of-a-female-hand-holding-a-pencil-against-a-sudoku-S1F2H9.jpg").convert()
    # Using blit to copy content from one surface to other
    screen.blit(imp, (0, 0))
    # paint screen one time
    pygame.display.flip()

    if win != 0:
        text = 'Game won!'
        game_over_surf = game_over_font.render(text, 0, WHITE)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
        screen.blit(game_over_surf, game_over_rect)

        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 30, exit_text.get_size()[1] + 30))
        exit_surface.fill(FILL)
        exit_surface.blit(exit_text, (15, 15))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(exit_surface, exit_rectangle)

    else:
        text = 'Game Over :('
        game_over_surf = game_over_font.render(text, 0, WHITE)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
        screen.blit(game_over_surf, game_over_rect)

        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 30, restart_text.get_size()[1] + 30))
        restart_surface.fill(FILL)
        restart_surface.blit(restart_text, (15, 15))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                elif restart_rectangle.collidepoint(event.pos):
                    pass

        pygame.display.update()
