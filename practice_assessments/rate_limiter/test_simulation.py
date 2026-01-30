import unittest
from simulation import simulate_coding_framework


class TestSimulateCodingFramework(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/users"],
            ["ALLOW_REQUEST", "bob", "/api/data"],
            ["GET_REQUEST_COUNT", "alice"],
            ["GET_REQUEST_COUNT", "bob"],
            ["GET_REQUEST_COUNT", "charlie"],
            ["CLEAR_USER", "alice"],
            ["GET_REQUEST_COUNT", "alice"],
            ["GET_REQUEST_COUNT", "bob"],
        ]
        self.test_data_2 = [
            ["SET_LIMIT", "/api/data", "3"],
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/data"],
            ["ALLOW_REQUEST", "bob", "/api/data"],
            ["ALLOW_REQUEST", "alice", "/api/users"],
            ["GET_ENDPOINT_COUNT", "alice", "/api/data"],
            ["GET_ENDPOINT_COUNT", "alice", "/api/users"],
            ["GET_ENDPOINT_COUNT", "bob", "/api/data"],
            ["GET_REQUEST_COUNT", "alice"],
        ]
        self.test_data_3 = [
            ["SET_LIMIT_AT", "1000", "/api/data", "3", "60"],
            ["ALLOW_REQUEST_AT", "1010", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1020", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1030", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1040", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1080", "alice", "/api/data"],
            ["GET_REQUEST_COUNT_AT", "1080", "alice"],
            ["GET_ENDPOINT_COUNT_AT", "1080", "alice", "/api/data"],
            ["GET_REQUEST_COUNT_AT", "1200", "alice"],
        ]
        self.test_data_4 = [
            ["SET_LIMIT_AT", "1000", "/api/data", "5", "60"],
            ["ALLOW_REQUEST_AT", "1010", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1020", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1030", "alice", "/api/data"],
            ["ALLOW_REQUEST_AT", "1010", "bob", "/api/data"],
            ["ALLOW_REQUEST_AT", "1020", "bob", "/api/users"],
            ["RATE_LIMIT_STATUS_AT", "2000", "alice", "/api/data", "1025"],
            ["RATE_LIMIT_STATUS_AT", "2000", "alice", "/api/data", "1050"],
            ["RATE_LIMIT_STATUS_AT", "2000", "bob", "/api/users", "1025"],
            ["RATE_LIMIT_STATUS_AT", "2000", "alice", "/api/data", "1075"],
        ]

    def test_group_1(self):
        output = simulate_coding_framework(self.test_data_1)
        self.assertEqual(output, ["allowed", "allowed", "allowed", "allowed", "count 3", "count 1", "count 0", "cleared alice", "count 0", "count 1"])

    def test_group_2(self):
        output = simulate_coding_framework(self.test_data_2)
        self.assertEqual(output, ["limit set /api/data 3", "allowed", "allowed", "allowed", "denied", "allowed", "allowed", "count 3", "count 1", "count 1", "count 4"])

    def test_group_3(self):
        output = simulate_coding_framework(self.test_data_3)
        self.assertEqual(output, ["limit set /api/data 3 60", "allowed", "allowed", "allowed", "denied", "allowed", "count 2", "count 2", "count 0"])

    def test_group_4(self):
        output = simulate_coding_framework(self.test_data_4)
        self.assertEqual(output, ["limit set /api/data 5 60", "allowed", "allowed", "allowed", "allowed", "allowed", "2/5", "3/5", "1/unlimited", "2/5"])


if __name__ == '__main__':
    unittest.main()
