import unittest
from simulation import simulate_coding_framework


class TestSimulateCodingFramework(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["CREATE_EVENT", "e1", "10", "20"],
            ["CREATE_EVENT", "e2", "30", "40"],
            ["CREATE_EVENT", "e3", "50", "60"],
            ["GET_EVENT", "e1"],
            ["GET_EVENT", "e4"],
            ["DELETE_EVENT", "e2"],
            ["GET_EVENT", "e2"],
            ["GET_EVENT", "e3"],
        ]
        self.test_data_2 = [
            ["CREATE_EVENT", "e1", "10", "20"],
            ["CREATE_EVENT", "e2", "15", "25"],
            ["CREATE_EVENT", "e2", "20", "30"],
            ["CREATE_EVENT", "e3", "5", "10"],
            ["CREATE_EVENT", "e4", "25", "35"],
            ["CREATE_EVENT", "e4", "30", "40"],
            ["EVENTS_IN_RANGE", "8", "22"],
            ["NEXT_EVENT", "18"],
            ["NEXT_EVENT", "40"],
        ]
        self.test_data_3 = [
            ["CREATE_EVENT", "e1", "100", "110"],
            ["CREATE_RECURRING", "r1", "200", "210", "50"],
            ["CREATE_EVENT", "e2", "255", "265"],
            ["CREATE_EVENT", "e2", "260", "270"],
            ["GET_OCCURRENCES", "r1", "190", "320"],
            ["GET_OCCURRENCES", "e1", "50", "150"],
            ["EVENTS_IN_RANGE", "245", "275"],
            ["NEXT_EVENT", "305"],
        ]
        self.test_data_4 = [
            ["CREATE_EVENT", "e1", "100", "200", "alice"],
            ["CREATE_EVENT", "e2", "150", "250", "bob"],
            ["CREATE_EVENT", "e3", "180", "220", "alice"],
            ["CREATE_EVENT", "e3", "200", "300", "alice"],
            ["CREATE_RECURRING", "r1", "400", "430", "100", "alice"],
            ["CREATE_RECURRING", "r2", "500", "540", "200", "bob"],
            ["USER_SCHEDULE", "alice", "90", "550"],
            ["USER_SCHEDULE", "bob", "100", "600"],
            ["FIND_FREE_TIME", "alice", "90", "550", "80"],
            ["FIND_FREE_TIME", "alice", "90", "550", "200"],
            ["FIND_FREE_TIME", "bob", "100", "600", "100"],
        ]

    def test_group_1(self):
        output = simulate_coding_framework(self.test_data_1)
        self.assertEqual(output, ["created e1", "created e2", "created e3", "event e1 10 20", "not found", "deleted e2", "not found", "event e3 50 60"])

    def test_group_2(self):
        output = simulate_coding_framework(self.test_data_2)
        self.assertEqual(output, ["created e1", "conflict e2", "created e2", "created e3", "conflict e4", "created e4", "events [e3, e1, e2]", "next e2", "none"])

    def test_group_3(self):
        output = simulate_coding_framework(self.test_data_3)
        self.assertEqual(output, ["created e1", "created r1", "conflict e2", "created e2", "occurrences [200-210, 250-260, 300-310]", "occurrences [100-110]", "events [r1, e2]", "next r1"])

    def test_group_4(self):
        output = simulate_coding_framework(self.test_data_4)
        self.assertEqual(output, ["created e1", "created e2", "conflict e3", "created e3", "created r1", "created r2", "schedule [e1:100-200, e3:200-300, r1:400-430, r1:500-530]", "schedule [e2:150-250, r2:500-540]", "free 300-380", "no availability", "free 250-350"])


if __name__ == '__main__':
    unittest.main()
