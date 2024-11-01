import unittest
from player import Player
from statistics_service import StatisticsService

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
    
    def test_search_player_found(self):
        result = self.stats.search("Semenko")
        self.assertAlmostEqual(str(result), f"{Player("Semenko", "EDM", 4, 12)}")
    
    def test_search_player_not_found(self):
        result = self.stats.search("Semekenko")
        self.assertAlmostEqual(result, None)
    
    def test_players_of_team(self):
        result = [str(pl) for pl in self.stats.team("EDM")]
        expected = [str(Player("Semenko", "EDM", 4, 12)),
                    str(Player("Kurri",   "EDM", 37, 53)),
                    str(Player("Gretzky", "EDM", 35, 89))]

        self.assertAlmostEqual(result, expected)
    
    def test_top_player(self):
        result = [str(pl) for pl in self.stats.top(4)]
        expected = [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Lemieux", "PIT", 45, 54)),
            str(Player("Yzerman", "DET", 42, 56)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Semenko", "EDM", 4, 12))   
        ]
        self.assertAlmostEqual(result,expected)
