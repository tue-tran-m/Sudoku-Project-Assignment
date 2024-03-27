class Board:
    def __init__(self, width, height, screen, difficulty, rows, cols):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()
        self.cells = [
            [Cell(self.board[i][j], i, j, SQUARE_SIZE, SQUARE_SIZE) for j in range(cols)]
            for i in range(rows)]

    def draw(self, screen):  # BOARDINIT.DRAW ONLY GENERATES THE LINES NOTHING ELSE.
        for i in range(1, BOARD_COLS + 1):
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

    def row_is_valid(self):
        for i in range(9):
            if len(set(self.board[i])) == 9:
                continue
            else:
                return False
        return True

    def col_is_valid(self):
        for i in range(9):
            col = [item[i] for item in sudoku]
            if len(set(col)) == 9:
                continue
            else:
                return False

        return True

    def cell_is_valid(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                value = self.board[i][j: j + 3]
                value.extend(self.board[i + 1][j: j + 3])
                value.extend(self.board[i + 2][j: j + 3])
                if len(set(value)) == 9:
                    continue
                else:
                    return False
        return True

    def check_board(self):
        return self.row_is_valid() and self.col_is_valid() and self.cell_is_valid()