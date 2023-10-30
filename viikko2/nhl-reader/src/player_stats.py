class PlayerStats():
    def __init__(self, reader):
        self.reader = reader
        self._players = self.reader.get_players()

    def top_scrorers_by_nationality(self, nationality):
        players = list(
            filter(lambda x: x.nationality == nationality, self._players))

        return sorted(players, key=lambda x: x.points, reverse=True)
