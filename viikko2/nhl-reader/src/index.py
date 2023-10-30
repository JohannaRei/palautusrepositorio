import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    players_from_finland = list(
        filter(lambda x: x.nationality == "FIN", players))

    for player in sorted(players_from_finland, key=lambda x: x.points, reverse=True):
        print(player)


if __name__ == "__main__":
    main()
