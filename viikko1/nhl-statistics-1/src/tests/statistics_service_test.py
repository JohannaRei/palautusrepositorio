import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_asettaa_pelaajat(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_search_palauttaa_haetun_pelaajan(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_ei_loyda_pelaajaa(self):
        player = self.stats.search("Tuntematon")
        self.assertAlmostEqual(player, None)

    def test_team_palauttaa_oikean_maaran_pelaajia(self):
        players = self.stats.team("EDM")
        self.assertAlmostEqual(len(players), 3)

    def test_top_ilman_hakuperustetta_palauttaa_oikean_pelaajan(self):
        player = self.stats.top(1)[0]
        self.assertEqual(player.name, "Gretzky")

    def test_top_goals_palauttaa_oikean_pelaajan(self):
        player = self.stats.top(1, SortBy.GOALS)[0]
        self.assertEqual(player.name, "Lemieux")

    def test_top_assists_palauttaa_oikean_pelaajan(self):
        player = self.stats.top(1, SortBy.ASSISTS)[0]
        self.assertEqual(player.name, "Gretzky")
