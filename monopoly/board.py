class Board:
    def __init__(self, players, properties, bonus=100):
        self.players = {p: -1 for p in players}
        self.properties = properties
        self.bonus = bonus

    def move(self, player, steps):
        cur_pos = self.players[player]
        new_lap, new_pos = divmod(cur_pos + steps, len(self))
        self.players[player] = new_pos

        if new_lap:
            player.receive(self.bonus)

        return self.properties[new_pos]

    def __len__(self):
        return len(self.properties)

    def remove(self, player):
        del self.players[player]
