from pprint import pprint

class Arena(object):
    dimx, dimy = (15, 15)
    arena = [['X' for _ in range(dimx)] for _ in range(dimy)]
    bullets = []

    def __init__(self, dim):
        self.dimx, self.dimy = dim
        self.arena = [['X' for _ in range(self.dimx)] for _ in range(self.dimy)]

    def reset(self):
        self.arena = [['X' for _ in range(self.dimx)] for _ in range(self.dimy)]

    def mark_player(self, position):
        self.arena[position[1]][position[0]] = '0'

    def mark_bullet(self, position):
        self.arena[position[1]][position[0]] = '!'

    def erase(self, position):
        self.arena[position[1]][position[0]] = 'X'

class Bullet(object):
    direction = 'n'
    Bl_spd = 2
    Bl_position = []

    def __init__(self, direction, Bl_spd, Bl_position):
        self.direction = direction
        self.Bl_spd = Bl_spd
        self.Bl_position = Bl_position

    def move(self):
        dist = {
        'w': (0, -self.Bl_spd),
        'a': (-self.Bl_spd, 0),
        's': (0, self.Bl_spd),
        'd': (self.Bl_spd, 0),
        'n': (0, 0)
        }
        self.Bl_position = [self.Bl_position[0] + dist[self.direction][0], self.Bl_position[1] + dist[self.direction][1]]

class Fighter(Bullet):
    name = "Player"
    hp, att, arm, vit, spd, mvmt = (10, 1, 0, 0, 1, 1)
    position = [0, 0]

    def __init__(self, name, stats, position):
        self.name = name
        self.hp, self.att, self.arm, self.vit, self.spd, self.mvmt = stats
        self.position = position

    def take_turn(self, action):
        a = {'Attack': self.attack, 'Move': self.move}
        a[action]()

    def attack(self):
        direction = raw_input('Direction: ')
        game.bullets.append(Bullet(direction, 2, self.position))

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

def start_loop(players):
    global game
    game = Arena([15, 10])
    game.mark_player(players[0].position)
    game.mark_player(players[1].position)
    while True:
        for i in range(len(players)):
            game.erase(players[i].position)
            action = raw_input("\nAction: ")
            players[i].take_turn(action)

            try:
                game.mark_player(players[i].position)
            except IndexError:
                print "Invalid, cannot move out of arena"

            print '\n'

        for i in range(len(game.bullets)):
            game.erase(game.bullets[i].Bl_position)
            game.bullets[i].move()

            try:
                game.mark_bullet(game.bullets[i].Bl_position)
            except IndexError:
                game.erase(game.bullets[i].Bl_position)

        for row in game.arena:
                print row


a = Fighter('Kylui', [999, 999 ,999 ,999, 999, 5], [0, 0])
b = Fighter('Justang', [6969, 69, 69, 69, 69, 5], [14, 9])

players = [a, b]

if __name__ == '__main__':
    start_loop(players)
