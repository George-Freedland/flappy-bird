class Util:
    def checkCollision(self, enemies, player):
        for enemy in enemies:
            if (player.x >= enemy.x and player.x <= enemy.x + 100):
                if(player.y >= 0 and player.y + 10 <= enemy.topLength):
                    return True
            if (player.x + 60 >= enemy.x and player.x + 60 <= enemy.x + 100):
                if(player.y >= 0 and player.y + 10 <= enemy.topLength):
                    return True
            if (player.x >= enemy.x and player.x <= enemy.x + 100):
                if(player.y + 60 >= 0 and player.y + 54 <= enemy.topLength):
                    return True
            if (player.x + 60 >= enemy.x and player.x + 60 <= enemy.x + 100):
                if(player.y + 54 >= 0 and player.y + 54 <= enemy.topLength):
                    return True

            if (player.x >= enemy.x and player.x <= enemy.x + 100):
                if(player.y >= enemy.topLength + 200 and player.y + 10 <= 900):
                    return True
            if (player.x + 60 >= enemy.x and player.x + 60 <= enemy.x + 100):
                if(player.y >= enemy.topLength + 200 and player.y + 10 <= 900):
                    return True
            if (player.x >= enemy.x and player.x <= enemy.x + 100):
                if(player.y + 54 >= enemy.topLength + 200 and player.y + 54 <= 900):
                    return True
            if (player.x + 60 >= enemy.x and player.x + 60 <= enemy.x + 100):
                if(player.y + 54 >= enemy.topLength + 200 and player.y + 54 <= 900):
                    return True

        return False