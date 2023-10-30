from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader(
            "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt")
    )
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)
    top_goals = stats.top(10, SortBy.GOALS)
    top_assists = stats.top(10, SortBy.ASSISTS)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)
    print("\n")

    print("Top point getters:")
    for player in top_scorers:
        print(player)
    print("\n")

    print("Top goal scorers:")
    for player in top_goals:
        print(player)
    print("\n")

    print("Top by assists:")
    for player in top_assists:
        print(player)


if __name__ == "__main__":
    main()
