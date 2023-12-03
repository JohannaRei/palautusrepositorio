score_names = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}


class PlayerScore:
    def __init__(self):
        self.score = 0

    def add_point(self):
        self.score += 1

    @property
    def value(self):
        return self.score

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        if self.score > 4:
            return "Game"
        return score_names[self.score]
