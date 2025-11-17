import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x=1

    while x==1:
        log_state()
        screen.fill("black")
        pygame.display.flip()   

if __name__ == "__main__":
    main()
