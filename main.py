import pygame

from Player import Player
from Score import Score
from GameOver import GameOver
from Enemy import Enemy
from TimeConfig import TimeConfig
from Util import Util
 
# ****************************************************************
# ENV Variables, will be in config file.
# ****************************************************************
# SCREEN_WIDTH = 1920
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 900

def main():
    # ****************************************************************
    # Initialize Pygame screen, screen size, name, and and logo
    # ****************************************************************
    pygame.init()
    logo = pygame.image.load('images/logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Flappy Bird")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     
    # ****************************************************************
    # Create Game Objects
    # ****************************************************************
    # Player
    player = Player()
    # Score
    score = Score()
    # Game Over
    gameOver = GameOver()

    # Enemy Array
    enemies = []
    enemies.append(Enemy(SCREEN_WIDTH))

    # Time configuration
    timeConfig = TimeConfig()

    # Util class
    util = Util()

    # ****************************************************************
    # Game Loop
    # ****************************************************************
    running = True
    while running:
        # Screen refresh
        screen.fill((200, 100, 100))

        # ****************************************************************
        # Event check loop
        # ****************************************************************
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN and not gameOver.getValue():
                if event.key == pygame.K_UP:
                    player.bounce()
            if event.type == pygame.KEYDOWN and gameOver.getValue() == True:
                if event.key == pygame.K_SPACE:
                    gameOver.setValue(False)
                    player.reset()
                    score.setValue(0)
                    enemies = []
                    enemies.append(Enemy(SCREEN_WIDTH))
                    timeConfig = TimeConfig()
               
        # ****************************************************************        
        # Handle Game Objects
        # ****************************************************************
        score.show(screen)
        player.show(screen)

        if timeConfig.timeToMakeEnemy() == True:
            enemies.append(Enemy(SCREEN_WIDTH))

        collision = False

        collision = util.checkCollision(enemies, player)

        for enemy in enemies:
            enemy.show(screen)
            if enemy.x == player.x and collision == False:
                score.increase()

        if player.outOfBounds() or collision == True:
            gameOver.setValue(True)

        if gameOver.getValue() == True:
            player.stop()
            for enemy in enemies: enemy.stop()
            gameOver.show(screen)

        # ****************************************************************
        # Update Display
        # ****************************************************************
        pygame.display.update()

# ****************************************************************
# Main Entry Point
# ****************************************************************     
if __name__=="__main__":
    main()
