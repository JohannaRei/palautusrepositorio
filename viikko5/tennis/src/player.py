from score import PlayerScore


class Player:
    def __init__(self, name):
        self.name = name
        self.points = PlayerScore()

    def win_point(self):
        self.points.add_point()

    @property
    def score(self):
        return self.points
