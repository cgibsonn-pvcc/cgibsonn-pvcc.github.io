import pygame
XLIMIT, YLIMIT = 650, 650
WIN = pygame.display.set_mode((XLIMIT, YLIMIT))
pygame.display.set_caption("CyberSnake")

def SnakeGameplay():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((100, 255, 255))
        
    pygame.quit()
    
if __name__ == "__SnakeGameplay__":
    SnakeGameplay()
