def draw_game_start(screen):

    # Initialize title font
    start_title_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 40)

    # Color background
    imp = pygame.image.load("/Users/mt/Downloads/a-close-up-shot-of-a-female-hand-holding-a-pencil-against-a-sudoku-S1F2H9.jpg").convert()
    # Using blit to copy content from one surface to other
    screen.blit(imp, (0, 0))
    # paint screen one time
    pygame.display.flip()

    # Initialize and draw title
    title_surface = start_title_font.render("WELCOME TO SUDOKU", 0, WHITE)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw sub-title
    sub_title_surface = start_title_font.render("Select Game Mode:", 0, WHITE)
    sub_title_rectangle = sub_title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(sub_title_surface,sub_title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 30, easy_text.get_size()[1] + 30))
    easy_surface.fill(FILL)
    easy_surface.blit(easy_text, (15, 15))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 30, medium_text.get_size()[1] + 30))
    medium_surface.fill(FILL)
    medium_surface.blit(medium_text, (15, 15))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 30, hard_text.get_size()[1] + 30))
    hard_surface.fill(FILL)
    hard_surface.blit(hard_text, (15, 15))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE * 7))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, SQUARE_SIZE * 7))
    hard_rectangle = hard_surface.get_rect(
        center=(SQUARE_SIZE * 7 + SQUARE_SIZE // 2 , SQUARE_SIZE * 7))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 30)
                    board.draw()
                elif medium_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 40)
                    board.draw()
                elif hard_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 50)
                    board.draw()
        pygame.display.update()
