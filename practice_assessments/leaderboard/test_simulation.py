import unittest
from simulation import simulate_coding_framework


class TestSimulateCodingFramework(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["ADD_SCORE", "SpaceRace", "alice", "1500"],
            ["ADD_SCORE", "SpaceRace", "alice", "1200"],
            ["ADD_SCORE", "SpaceRace", "bob", "1800"],
            ["GET_TOP_SCORE", "SpaceRace", "alice"],
            ["GET_TOP_SCORE", "SpaceRace", "charlie"],
            ["REMOVE_PLAYER", "SpaceRace", "alice"],
            ["GET_TOP_SCORE", "SpaceRace", "alice"],
            ["GET_TOP_SCORE", "SpaceRace", "bob"],
        ]
        self.test_data_2 = [
            ["ADD_SCORE", "SpaceRace", "alice", "1500"],
            ["ADD_SCORE", "SpaceRace", "bob", "1800"],
            ["ADD_SCORE", "SpaceRace", "charlie", "1500"],
            ["ADD_SCORE", "SpaceRace", "alice", "1200"],
            ["GET_TOP_PLAYERS", "SpaceRace", "3"],
            ["GET_PLAYER_RANK", "SpaceRace", "alice"],
            ["GET_PLAYER_RANK", "SpaceRace", "dave"],
        ]
        self.test_data_3 = [
            ["ADD_SCORE_AT", "1000", "SpaceRace", "alice", "1500"],
            ["ADD_SCORE_AT", "1000", "SpaceRace", "bob", "1800", "60"],
            ["ADD_SCORE_AT", "1005", "SpaceRace", "alice", "1600", "100"],
            ["GET_TOP_SCORE_AT", "1050", "SpaceRace", "alice"],
            ["GET_TOP_SCORE_AT", "1050", "SpaceRace", "bob"],
            ["GET_TOP_SCORE_AT", "1070", "SpaceRace", "bob"],
            ["GET_TOP_PLAYERS_AT", "1050", "SpaceRace", "2"],
            ["REMOVE_PLAYER_AT", "1055", "SpaceRace", "alice"],
            ["GET_PLAYER_RANK_AT", "1056", "SpaceRace", "bob"],
        ]
        self.test_data_4 = [
            ["ADD_SCORE_AT", "100", "SpaceRace", "alice", "1500"],
            ["ADD_SCORE_AT", "200", "SpaceRace", "bob", "1800"],
            ["ADD_SCORE_AT", "300", "SpaceRace", "charlie", "2000", "150"],
            ["ADD_SCORE_AT", "400", "SpaceRace", "dave", "1700"],
            ["REMOVE_PLAYER_AT", "500", "SpaceRace", "bob"],
            ["LEADERBOARD_AT", "600", "SpaceRace", "250", "3"],
            ["LEADERBOARD_AT", "600", "SpaceRace", "450", "3"],
            ["LEADERBOARD_AT", "600", "SpaceRace", "550", "3"],
        ]

    def test_group_1(self):
        output = simulate_coding_framework(self.test_data_1)
        self.assertEqual(output, ["added alice 1500", "added alice 1200", "added bob 1800", "top alice 1500", "not found", "removed alice", "not found", "top bob 1800"])

    def test_group_2(self):
        output = simulate_coding_framework(self.test_data_2)
        self.assertEqual(output, ["added alice 1500", "added bob 1800", "added charlie 1500", "added alice 1200", "top players [bob:1800, alice:1500, charlie:1500]", "rank alice 2", "not found"])

    def test_group_3(self):
        output = simulate_coding_framework(self.test_data_3)
        self.assertEqual(output, ["added at alice 1500", "added at bob 1800", "added at alice 1600", "top at alice 1600", "top at bob 1800", "not found", "top players at [bob:1800, alice:1600]", "removed at alice", "rank at bob 1"])

    def test_group_4(self):
        output = simulate_coding_framework(self.test_data_4)
        self.assertEqual(output, ["added at alice 1500", "added at bob 1800", "added at charlie 2000", "added at dave 1700", "removed at bob", "leaderboard at [bob:1800, alice:1500]", "leaderboard at [bob:1800, dave:1700, alice:1500]", "leaderboard at [dave:1700, alice:1500]"])


if __name__ == '__main__':
    unittest.main()
