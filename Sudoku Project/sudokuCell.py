from constants import *
import pygame

class Cell:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def set_cell_value(self, val):
        self.value = val
        pygame.draw.rect(screen, (0, 0, 0), (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)  # SETS OLD SELECTED CELL BACK TO BLACK TO INDICATE NO LONGER SELECTED
        x, y = event.pos
        self.row = y // SQUARE_SIZE
        self.col = x // SQUARE_SIZE
        pygame.draw.rect(screen, RED_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)  # SETS SELECTED CELL TO RED OUTLINE TO INDICATE SELECTION

    def replace_cell(self):
        pygame.draw.rect(screen, BG_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, RED_COLOR, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)



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

        if self.value == '1':      # THE FOLLOWING STATEMENTS ALL GENERATE A NUMBER WITHIN A CELL THAT HAS A DETERMINED VALUE. MUST IMPLEMENT DRAW AFTER EVERYTIME (BOX SELECTED AND A CELL VALUE) IS IMPLEMENTED BY USER.
            ex1.replace_cell()
            num_1_rect = num_1_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_1_surf, num_1_rect)

        elif self.value == '2':
            ex1.replace_cell()
            num_2_rect = num_2_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_2_surf, num_2_rect)
        elif self.value == '3':
            ex1.replace_cell()
            num_3_rect = num_3_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_3_surf, num_3_rect)
        elif self.value == '4':
            ex1.replace_cell()
            num_4_rect = num_4_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_4_surf, num_4_rect)
        elif self.value == '5':
            ex1.replace_cell()
            num_5_rect = num_5_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_5_surf, num_5_rect)
        elif self.value == '6':
            ex1.replace_cell()
            num_6_rect = num_6_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_6_surf, num_6_rect)
        elif self.value == '7':
            ex1.replace_cell()
            num_7_rect = num_7_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_7_surf, num_7_rect)
        elif self.value == '8':
            ex1.replace_cell()
            num_8_rect = num_8_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_8_surf, num_8_rect)
        elif self.value == '9':
            ex1.replace_cell()
            num_9_rect = num_9_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num_9_surf, num_9_rect)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)

    ex1 = Cell('0', 150, 150, SQUARE_SIZE, SQUARE_SIZE)
    ex1.draw(screen)
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                ex1.set_cell_value(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ex1.value = "1"
                if event.key == pygame.K_2:
                    ex1.value = "2"
                if event.key == pygame.K_3:
                    ex1.value = "3"
                if event.key == pygame.K_4:
                    ex1.value = "4"
                if event.key == pygame.K_5:
                    ex1.value = "5"
                if event.key == pygame.K_6:
                    ex1.value = "6"
                if event.key == pygame.K_7:
                    ex1.value = "7"
                if event.key == pygame.K_8:
                    ex1.value = "8"
                if event.key == pygame.K_9:
                    ex1.value = "9"
                ex1.draw(screen)
        pygame.display.update()