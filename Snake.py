import pygame
XLIMIT, YLIMIT = 650, 650
WIN = pygame.display.set_mode((XLIMIT, YLIMIT))
pygame.display.set_caption("CyberSnake")

CYAN = (100, 255, 255)

FRAMESPERSECOND = 60

def drawings_on_window():
    WIN.fill(CYAN)
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FRAMESPERSECOND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawings_on_window()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
