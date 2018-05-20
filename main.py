from pprint import pprint

class Fighter(object):
    name = "Player"
    hp, att, arm, vit, spd, mvmt = (10, 1, 0, 0, 1, 1)
    position = [0, 0]

    def __init__(self, name, stats, position):
        self.name = name
        self.hp, self.att, self.arm, self.vit, self.spd, self.mvmt = stats
        self.position = position

    def take_turn(self, action):
        a = {'attack': self.attack, 'move': self.move}
        a[action]()

    def attack(self):
        return self.att

    def move(self):
        vec = str(raw_input('Move: ')).split(' ')

        if len(vec) > 2 or len(vec) < 0:
            print "Invalid, too large/small size or not list"
            self.move()

        distx = int(vec[0])
        disty = int(vec[1])

        if abs(distx) <= self.mvmt or abs(disty) <= self.mvmt:
            self.regen()
            self.position = [self.position[0] + distx, self.position[1] + disty]
        else:
            print "Invalid, cannot travel that far"

    def regen(self):
        self.hp += self.vit

    def take_dmg(self, dmg):
        self.hp -= (dmg + self.arm)

class Arena(object):
    dimx, dimy = (15, 15)
    arena = [['X' for _ in range(dimx)] for _ in range(dimy)]

    def __init__(self, dim):
        self.dimx, self.dimy = dim
        self.arena = [['X' for _ in range(self.dimx)] for _ in range(self.dimy)]

    def reset(self):
        self.arena = [['X' for _ in range(self.dimx)] for _ in range(self.dimy)]

    def mark(self, position):
        self.arena[position[0]][position[1]] = '0'

    def erase(self, position):
        self.arena[position[0]][position[1]] = 'X'

class Bullet(object):
    

def start_loop(players):
    game = Arena([15, 10])
    game.mark(players[0].position)
    game.mark(players[1].position)
    while True:
        for i in range(len(players)):
            game.erase(players[i].position)
            action = raw_input("\nAction: ")
            players[i].take_turn(action)
            try:
                game.mark(players[i].position)
            except IndexError:
                print "Invalid, cannot move out of arena"
            print '\n'
            for row in game.arena:
                print row


a = Fighter('Kylui', [999, 999 ,999 ,999, 999, 5], [0, 0])
b = Fighter('Justang', [6969, 69, 69, 69, 69, 5], [9, 14])

players = [a, b]

if __name__ == '__main__':
    start_loop(players)
