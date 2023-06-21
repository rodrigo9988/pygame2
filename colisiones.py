from player import *
from enemy import *
from disparo_player import *


class Colisiones:
    def __init__(self, game, player, balas_player, enemy, balas_enemy, score):
        self.game = game
        self.player = player
        self.balas_player = balas_player
        self.enemy = enemy
        self.balas_enemy = balas_enemy
        self.score = score
        self.score = 0

    def verificar_colisiones(self, score):
        # Colisiones entre las balas del jugador y los enemigos
        for bala in self.balas_player:
            for enemy in self.enemy:
                if bala.rect.colliderect(enemy.rect):
                    self.enemy.remove(enemy)
                    self.balas_player.remove(bala)
                    score += 100     
            
        for enemy in self.enemy:
            if enemy.rect.colliderect(self.player.rect):
                self.enemy.remove(enemy)
                self.player.vidas = 0

        # Colisiones entre las balas enemigas y el jugador
        #if hasattr(self.player, 'rect'):
        for bala in self.balas_enemy:
            if bala.rect.colliderect(self.player):    
                self.balas_enemy.remove(bala)
                self.player.vidas -= 1
        return score


    
