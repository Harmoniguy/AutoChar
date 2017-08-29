import pickle


class Player:
    def __init__(self, name):
        self.name = name
        self.noun = ''
        self.descriptor = ''
        self.focus = ''
        self.level = 0
        self.experience_points = 0
        self.speed_pool = 0
        self.might_pool = 0
        self.int_pool = 0
        self.speed_edge = 0
        self.might_edge = 0
        self.int_edge = 0
        self.int = 0
        self.might = 0
        self.speed = 0
        self.notes = ""


class PlayerStore:
    def __init__(self):
        self.filenames = {}

    def save(self, player, filename):
        with open(filename, 'wb') as f:
            pickle.dump(player, f)
            self.filenames[player] = filename

    def update(self, player):
        filename = self.filenames[player]
        with open(filename, 'wb') as f:
            pickle.dump(player, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            player = pickle.load(f)
            self.filenames[player] = filename
            return player


store = PlayerStore()
player1 = Player('Zach')
player1.noun = 'Wizard'
player2 = Player('Joe')
player2.noun = 'Wizard'
player2.descriptor = "clever"
player2.focus = "stinks forever"
store.save(player1, 'player1.p')
store.save(player2, 'player2.p')
player1.speed += 10
store.update(player1)

###

store2 = PlayerStore()
store2.load('player1.p')
store2.load('player2.p')
for player, filename in store2.filenames.items():
    print(player.name, player.descriptor, player.noun, player.focus, filename)