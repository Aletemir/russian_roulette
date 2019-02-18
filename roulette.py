from player import Player
import random


class Roulette:
    def __init__(self):
        self.player = Player()
        self.barillet = 7
        self.number_player = 0
        self.bullet = 0
        self.round = 0
        self.rand_bullet = 0
        self.trigger = 0
        self.alive = True

    def initalize_game(self):
        self.number_player = int(input('Combien de joueurs êtes vous ? :\n'))

    def set_bullet(self):
        self.bullet = int(input('Avec combien de balles voulez vous jouer ? Maximum 6 \n'))
        if self.bullet == 1:
            print('Vous jouez avec {0} balle sur 6. Bon courage et bonne chance'.format(self.bullet))
        elif 1 < self.bullet < 5:
            print('Vous jouez avec {0} balles sur 6. Bon courage et bonne chance'.format(self.bullet))
        elif self.bullet <= 6:
            self.bullet = 6
            print(
                'Hoho, vous êtes TRES joueur, vous jouez avec {0} sur 6. Bon et bien ravie de vous avoir connus.'.format(
                    self.bullet))
        self.barillet -= self.bullet

    def random_bullet(self):
        self.rand_bullet = random.randint(1, self.barillet)

    def pull_trigger(self):
        pull = input('Appuyer sur la gachette = p \n')
        if pull == 'p':
            self.trigger += 1
            print('*Click*')
            self.round += 1

    def shot(self):
        if self.trigger == self.rand_bullet:
            print("Bang !")
            print('Bon et bien il va falloir nettoyer.')
            self.alive = False

    def play(self):
        # self.initalize_game()
        self.player.set_username()
        self.set_bullet()
        self.random_bullet()
        print('Prêt ? Commençons.')
        print('*rolling* *Clack*')
        while self.alive:
            self.pull_trigger()
            self.shot()


if __name__ == '__main__':
    game = Roulette()
    game.player.set_username()
    game.set_bullet()
    game.random_bullet()
    print('Prêt ? Commençons.')
    while game.alive:
        game.pull_trigger()
        if game.shot():
            game.shot()
