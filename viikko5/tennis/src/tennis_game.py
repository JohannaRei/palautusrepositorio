from player import Player


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def add_point_for_player(self, player_name):
        if player_name == "player1":
            self.player1.win_point()
        else:
            self.player2.win_point()

    def get_game_score(self):
        score1 = self.player1.score
        score2 = self.player2.score

        # Players' scores are tied
        if score1 == score2:
            if score1.value > 2:
                return 'Deuce'
            return f'{score1}-All'

        # One player has won or has advantage
        if score1.value >= 4 or score2.value >= 4:
            minus_result = score1.value - score2.value
            result = "Win for" if abs(minus_result) >= 2 else "Advantage"

            if minus_result >= 0:
                return f'{result} player1'
            return f'{result} player2'

        # Both players have points
        return f'{score1}-{score2}'
