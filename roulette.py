from player import Player
import random


class Roulette:
    def __init__(self):
        self.player = Player()
        self.barillet = 6
        self.number_player = 0
        self.bullet = 0
        self.round = 0
        self.rand_bullet = 0
        self.trigger = 0

    def initalize_game(self):
        self.number_player = int(input('Combien de joueurs êtes vous ? :\n'))

    def set_bullet(self):
        self.bullet = int(input('Avec combien de balles voulez vous jouer ? Maximum 6 \n'))

        if self.bullet == 1:
            self.bullet = self.bullet
            print('Vous jouez avec {0} balle sur {1}. Bon courage et bonne chance'.format(self.bullet, self.barillet))
        elif 1 < self.bullet <= self.barillet:
            self.bullet = self.bullet
            print('Vous jouez avec {0} balles sur {1}. Bon courage et bonne chance'.format(self.bullet, self.barillet))
        else:
            self.bullet = 6
            print(
                'Hoho, vous êtes TRES joueur, vous jouez avec {0} sur {1}. Bon et bien ravie de vous avoir connus.'.format(
                    self.bullet, self.barillet))

    def random_bullet(self):
        self.rand_bullet = random.randint(1, 6)

    def pull_trigger(self):
        self.trigger += 1
