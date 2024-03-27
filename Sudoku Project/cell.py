from Constant import *
from sgn import *
import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (60, 60, 60)
L_GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)
NUMBER_FONT = 50
WIDTH = 630
HEIGHT = 700
LINE_DELINEATE_WIDTH = 5
LINE_WIDTH = 1
WIN_LINE_WIDTH = 15
BOARD_ROWS = 9
BOARD_COLS = 9
SQUARE_SIZE = 70
SCREEN_COLOR = (240,248,255)
LINE_COLOR = (0, 0, 0)
FILL = (245, 152, 66)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self):
        number_font = pygame.font.Font(None, NUMBER_FONT)
        cell_value_surf = number_font.render(str(self.value), 0, BLACK)
        sketched_value_surf = number_font.render(' ', 0, GRAY)
        if self.selected:
            pygame.draw.rect(screen, L_RED, pygame.Rect(self.row * SQUARE_SIZE, self.col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
            self.selected = False


        if self.value != 0:
            cell_value_rect = cell_value_surf.get_rect(
                center = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(cell_value_surf, cell_value_rect)
        else:
            sketched_value_rect = sketched_value_surf.get_rect(
                center = (SQUARE_SIZE * self.col + 15, SQUARE_SIZE * self.row + 20))
            screen.blit(sketched_value_surf, sketched_value_rect)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, self.difficulty)
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)]

    def draw(self):
        # Draw an outline of the Sudoku grid, width bold lines to delineate the 3x3 boxes
        # Draw every cell on this board
        screen.fill(SCREEN_COLOR)
        # draw grid
        # draw horizontal lines in the 3x3 boxes
        screen.fill(SCREEN_COLOR)
            # draw grid
            # draw horizontal lines in the 3x3 boxes
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )
            # draw vertical lines that delineate the 3x3 boxes
        for j in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, BOARD_COLS * SQUARE_SIZE),
                LINE_WIDTH
            )
            # draw horizontal lines that delineate the 3x3 boxes
        for i in range(3, BOARD_ROWS + 1, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_DELINEATE_WIDTH
            )
            # draw vertical lines that delineate the 3x3 boxes
        for j in range(3, BOARD_COLS, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, BOARD_COLS * SQUARE_SIZE),
                LINE_DELINEATE_WIDTH
            )
            # draw cells
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

        for i in range(9):
           for j in range(9):
               self.cells[i][j].draw()

    def select(self, row, col):
        #if self.board[row][col] == 0:
        self.cells[row][col].selected = True

    def click(self, x, y):
        # If a tuple of (x,y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None
        if y < WIDTH:
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            return (int(row), int(col))
        else:
            return None

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells
        self.update = [[Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)]
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
    """
    https://www.geeksforgeeks.org/python-display-images-with-pygame/
    """

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

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    draw_game_start(screen)
    board = Board(WIDTH, HEIGHT,screen, 30)
    board.draw()

    # print(board.cells[0][0])
    # board.cells[0][0].selected = True
    # board.select(1,1)


while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    pygame.display.update()