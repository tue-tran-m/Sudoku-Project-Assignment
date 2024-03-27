buttonfont = pygame.font.Font(None, 40)
keysurface = buttonfont.render('R = Restart    E = Exit    V = Reset', 0, (CHIP_FONT))
key_rectangle = keysurface.get_rect(center=(300, 650))
screen.blit(keysurface, key_rectangle)