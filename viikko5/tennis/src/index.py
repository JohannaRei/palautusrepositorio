from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_game_score())

    game.add_point_for_player("player1")
    print(game.get_game_score())

    game.add_point_for_player("player1")
    print(game.get_game_score())

    game.add_point_for_player("player2")
    print(game.get_game_score())

    game.add_point_for_player("player1")
    print(game.get_game_score())

    game.add_point_for_player("player1")
    print(game.get_game_score())


if __name__ == "__main__":
    main()
