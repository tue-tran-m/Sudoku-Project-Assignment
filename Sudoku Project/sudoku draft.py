import pygame
import constants
import math, random
import sys
def draw_game_start(screen):

    # Initialize title font
    start_title_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 40)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("WELCOME TO SUDOKU", 0, (0,0,0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw subtitle
    sub_title_surface = start_title_font.render("Select Game Mode:", 0, (0,0,0))
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
    easy_surface.fill((20,30,40))
    easy_surface.blit(easy_text, (15, 15))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 30, medium_text.get_size()[1] + 30))
    medium_surface.fill((20,30,40))
    medium_surface.blit(medium_text, (15, 15))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 30, hard_text.get_size()[1] + 30))
    hard_surface.fill((20,30,40))
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
        global difficulty
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 30)
                    board.draw(screen)
                    difficulty = "easy"
                elif medium_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 40)
                    board.draw(screen)
                    difficulty = "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    board = Board(WIDTH, HEIGHT, screen, 50)
                    board.draw(screen)
                    difficulty = "hard"
                return difficulty
        pygame.display.update()

def draw_game_over(win, screen):

    game_over_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 40)

    # Color background
    imp = pygame.image.load(
        "/Users/mt/Downloads/a-close-up-shot-of-a-female-hand-holding-a-pencil-against-a-sudoku-S1F2H9.jpg").convert()
    # Using blit to copy content from one surface to other
    screen.blit(imp, (0, 0))
    # paint screen one time
    pygame.display.flip()

    if win == 0:
        text = 'Game won!'
        game_over_surf = game_over_font.render(text, 0, (255, 255, 255))
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
        screen.blit(game_over_surf, game_over_rect)

        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 30, exit_text.get_size()[1] + 30))
        exit_surface.fill(BG_COLOR)
        exit_surface.blit(exit_text, (15, 15))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(exit_surface, exit_rectangle)

    else:
        text = 'Game Over :('
        game_over_surf = game_over_font.render(text, 0, (255, 255, 255))
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, SQUARE_SIZE * 2 + SQUARE_SIZE // 2))
        screen.blit(game_over_surf, game_over_rect)

        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 30, restart_text.get_size()[1] + 30))
        restart_surface.fill(BG_COLOR)
        restart_surface.blit(restart_text, (15, 15))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length
	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed
	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.board = [['-' for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))

    '''
	Returns a 2D python list of numbers which represents the board
	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes
	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            for column in row:
                print(column, end='')
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True
	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	Return: boolean
    '''

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True
	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box
	Return: boolean
    '''

    def valid_in_box(self, row, col, num):
        col_start = col - col % 3
        row_start = row - row % 3

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box
	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell
	Return: boolean
    '''

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	Return: None
    '''

    def unused_in_box(self, row, col, num):
        return self.valid_in_box(row, col, num)

    def fill_box(self, row_start, col_start):
        for col in range(row_start, row_start + 3):
            for row in range(col_start, col_start + 3):
                num = random.randint(1, 9)
                while not self.unused_in_box(row, col, num):
                    num = random.randint(1, 9)
                self.board[row][col] = num
        return self.board


    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)
	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)
        return self.board

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	Parameters:
	row, col specify the coordinates of the first empty (0) cell
	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again
	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        while self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                self.removed_cells -= 1
        return self.board


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    global holderboard, solvedboard
    holderboard = [[],[],[],[],[],[],[],[],[]]
    # initialboard = []
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    # solvedboard = sudoku.fill_values()
    solvedboard = sudoku.get_board()
    for i in range(0,9):
        for j in range(0,9):
            holderboard[i].append(sudoku.get_board()[i][j])
    sudoku.remove_cells()
    return sudoku.get_board()

WIDTH = 600
HEIGHT = 700
LINE_WIDTH = 5
WIN_LINE_WIDTH = 5
BOLD_LINE = 10
BOARD_ROWS = 9
BOARD_COLS = 9
SQUARE_SIZE = 66.666
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (0,0,0)
RED_COLOR = (255, 0, 0)
NUM_COLOR = (66, 66, 66)
CHIP_FONT = 40
GAME_OVER_FONT = 40


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()
        # self.cells = [
        #     [Cell(self.board[i][j], i, j, SQUARE_SIZE, SQUARE_SIZE) for j in range(9)] for i in range(9)]

    def draw(self, screen):
        for i in range(1, BOARD_COLS+1):
            if i == 3:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BOLD_LINE)
            elif i == 6:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BOLD_LINE)
            elif i == 9:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BOLD_LINE)
            else:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

        for j in range(1, BOARD_ROWS):
            if j == 3:
                pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, 600), BOLD_LINE)
            elif j == 6:
                pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, 600), BOLD_LINE)
            else:
                pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, 600), LINE_WIDTH)

    def initialize_board(self):
        return [['0' for i in range(BOARD_ROWS)] for j in range(BOARD_COLS)]


    def reset_to_original(self):
        pass

    def check_board(self):
        pass


    def button(self, text, pos, fontsize):
        font = pygame.font.SysFont(CHIP_FONT, fontsize)
        x, y = pos
        buttext = font.render(text, True, (66, 66, 66), (0, 0, 0))
        textbox = buttext.get_rect()
        textbox.center = (x, y)
        return screen.blit(buttext, textbox)


class Cell:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def set_cell_value(self, val):
        self.value = val
        if 0 <= self.row <= 8:
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                             3)  # SETS OLD SELECTED CELL BACK TO BLACK TO INDICATE NO LONGER SELECTED
        x, y = event.pos
        self.row = y // SQUARE_SIZE
        self.col = x // SQUARE_SIZE
        if 0 <= self.row <= 8:
            pygame.draw.rect(screen, RED_COLOR,
                             (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                             3)  # SETS SELECTED CELL TO RED OUTLINE TO INDICATE SELECTION

    def replace_cell(self):
        pygame.draw.rect(screen, BG_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, RED_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)

    def starter_cell(self):
        pygame.draw.rect(screen, BG_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, (255,255,255), (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                         2)

    def implement_value(self):
        boardinit.board[int(self.row)][int(self.col)] = self.value

    def implement_start(self):
        num_font = pygame.font.Font(None, CHIP_FONT)  # 1-9 FONT
        num_1_surf = num_font.render('1', 0, NUM_COLOR)  # creating all numbers 1-9 in the same color
        num_2_surf = num_font.render('2', 0, NUM_COLOR)
        num_3_surf = num_font.render('3', 0, NUM_COLOR)
        num_4_surf = num_font.render('4', 0, NUM_COLOR)
        num_5_surf = num_font.render('5', 0, NUM_COLOR)
        num_6_surf = num_font.render('6', 0, NUM_COLOR)
        num_7_surf = num_font.render('7', 0, NUM_COLOR)
        num_8_surf = num_font.render('8', 0, NUM_COLOR)
        num_9_surf = num_font.render('9', 0, NUM_COLOR)

        for i in range(0,9):
            for j in range(0,9):
                self.row = i
                self.col = j
                if boardinit.board[i][j] != 0:
                    if boardinit.board[i][j] == 1:
                        ex1.starter_cell()
                        default_rect = num_1_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_1_surf, default_rect)
                    elif boardinit.board[i][j] == 2:
                        ex1.starter_cell()
                        default_rect = num_2_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_2_surf, default_rect)
                    elif boardinit.board[i][j] == 3:
                        ex1.starter_cell()
                        default_rect = num_3_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_3_surf, default_rect)
                    elif boardinit.board[i][j] == 4:
                        ex1.starter_cell()
                        default_rect = num_4_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_4_surf, default_rect)
                    elif boardinit.board[i][j] == 5:
                        ex1.starter_cell()
                        default_rect = num_5_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_5_surf, default_rect)
                    elif boardinit.board[i][j] == 6:
                        ex1.starter_cell()
                        default_rect = num_6_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_6_surf, default_rect)
                    elif boardinit.board[i][j] == 7:
                        ex1.starter_cell()
                        default_rect = num_7_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_7_surf, default_rect)
                    elif boardinit.board[i][j] == 8:
                        ex1.starter_cell()
                        default_rect = num_8_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_8_surf, default_rect)
                    elif boardinit.board[i][j] == 9:
                        ex1.starter_cell()
                        default_rect = num_9_surf.get_rect(
                            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
                        screen.blit(num_9_surf, default_rect)


    def draw(self, screen):

        num_font = pygame.font.Font(None, CHIP_FONT)  # 1-9 FONT
        num_1_surf = num_font.render('1', 0, NUM_COLOR) #creating all numbers 1-9 in the same color
        num_2_surf = num_font.render('2', 0, NUM_COLOR)
        num_3_surf = num_font.render('3', 0, NUM_COLOR)
        num_4_surf = num_font.render('4', 0, NUM_COLOR)
        num_5_surf = num_font.render('5', 0, NUM_COLOR)
        num_6_surf = num_font.render('6', 0, NUM_COLOR)
        num_7_surf = num_font.render('7', 0, NUM_COLOR)
        num_8_surf = num_font.render('8', 0, NUM_COLOR)
        num_9_surf = num_font.render('9', 0, NUM_COLOR)



        if self.value == 0:
                ex1.implement_value()
                ex1.replace_cell()
        if self.value == 1:      # THE FOLLOWING STATEMENTS ALL GENERATE A NUMBER WITHIN A CELL THAT HAS A DETERMINED VALUE. MUST IMPLEMENT DRAW AFTER EVERYTIME (BOX SELECTED AND A CELL VALUE) IS IMPLEMENTED BY USER.
            ex1.implement_value()
            ex1.replace_cell()
            num_1_rect = num_1_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_1_surf, num_1_rect)
        elif self.value == 2:
            ex1.implement_value()
            ex1.replace_cell()
            num_2_rect = num_2_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_2_surf, num_2_rect)
        elif self.value == 3:
            ex1.implement_value()
            ex1.replace_cell()
            num_3_rect = num_3_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_3_surf, num_3_rect)
        elif self.value == 4:
            ex1.implement_value()
            ex1.replace_cell()
            num_4_rect = num_4_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_4_surf, num_4_rect)
        elif self.value == 5:
            ex1.implement_value()
            ex1.replace_cell()
            num_5_rect = num_5_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_5_surf, num_5_rect)
        elif self.value == 6:
            ex1.implement_value()
            ex1.replace_cell()
            num_6_rect = num_6_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_6_surf, num_6_rect)
        elif self.value == 7:
            ex1.implement_value()
            ex1.replace_cell()
            num_7_rect = num_7_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_7_surf, num_7_rect)
        elif self.value == 8:
            ex1.implement_value()
            ex1.replace_cell()
            num_8_rect = num_8_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_8_surf, num_8_rect)
        elif self.value == 9:
            ex1.implement_value()
            ex1.replace_cell()
            num_9_rect = num_9_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_9_surf, num_9_rect)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    draw_game_start(screen)
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    boardinit = Board(screen, WIDTH, HEIGHT, "")
    ex1 = Cell('', 150, 150, SQUARE_SIZE, SQUARE_SIZE) #Initializing the first default instance of a cell.

    if difficulty == "easy":
        boardinit.board = generate_sudoku(9, 1)

        # boardinit.board = holderboard
        ex1.implement_start()
    if difficulty == "medium":
        boardinit.board = generate_sudoku(9, 40)

        # boardinit.board = holderboard
        ex1.implement_start()
    if difficulty == "hard":
        boardinit.board = generate_sudoku(9, 50)

        # boardinit.board = holderboard
        ex1.implement_start()
    boardinit.draw(screen)

    game_over = False
    firstscreen = True

    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                ex1.set_cell_value(0)
                # board is full
                for row in range(9):
                    for col in range(9):
                        if boardinit.board[int(ex1.row)][int(ex1.col)] != 0:
                            if boardinit.board[row][col] == holderboard[row][col]:
                                game_over = True
                            else:
                                game_over = False
                                draw_game_over(1, screen)

                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                # if boardinit.board[int(ex1.row)][int(ex1.col)] != defaultboard[int(ex1.row)][int(ex1.col)]:
                    if boardinit.board[int(ex1.row)][int(ex1.col)] == 0:


                        if event.key == pygame.K_1:
                            ex1.value = 1                      #defaultboard / holderboard = sudoku.get_board() which actively updates the "defaultboard" need to find a way to make the board stay the same / retrieve the board manually once.
                        if event.key == pygame.K_2:
                            ex1.value = 2
                        if event.key == pygame.K_3:
                            ex1.value = 3
                        if event.key == pygame.K_4:
                            ex1.value = 4
                        if event.key == pygame.K_5:
                            ex1.value = 5
                        if event.key == pygame.K_6:
                            ex1.value = 6
                        if event.key == pygame.K_7:
                            ex1.value = 7
                        if event.key == pygame.K_8:
                            ex1.value = 8
                        if event.key == pygame.K_9:
                            ex1.value = 9
                        if event.key == pygame.K_BACKSPACE:
                            ex1.value = 0
                        ex1.draw(screen)
                        # print(int(boardinit.board[int(ex1.row)][int(ex1.col)]))
                    print(f"{int(boardinit.board[int(ex1.row)][int(ex1.col)])} : boardinit")
                    print(f"{int(holderboard[int(ex1.row)][int(ex1.col)])} : holderboard")
                    print(f"{holderboard} initial")
                    print(f"{boardinit.board}")

                    if int(boardinit.board[int(ex1.row)][int(ex1.col)]) != int(holderboard[int(ex1.row)][int(ex1.col)]):
                        if event.key == pygame.K_1:
                            ex1.value = 1
                        if event.key == pygame.K_2:
                            ex1.value = 2
                        if event.key == pygame.K_3:
                            ex1.value = 3
                        if event.key == pygame.K_4:
                            ex1.value = 4
                        if event.key == pygame.K_5:
                            ex1.value = 5
                        if event.key == pygame.K_6:
                            ex1.value = 6
                        if event.key == pygame.K_7:
                            ex1.value = 7
                        if event.key == pygame.K_8:
                            ex1.value = 8
                        if event.key == pygame.K_9:
                            ex1.value = 9
                        if event.key == pygame.K_BACKSPACE:
                            ex1.value = 0
                        ex1.draw(screen)
                    # Check whether is win
                    for row in range(9):
                        for col in range(9):
                            if boardinit.board[row][col] == holderboard[row][col]:
                                game_over = True
                            else:
                                draw_game_over(1, screen)
                                game_over = False
            if game_over:
                pygame.display.update()
                draw_game_over(0, screen)
            pygame.display.update()