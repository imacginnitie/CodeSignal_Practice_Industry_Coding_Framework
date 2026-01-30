import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict


class Leaderboard:
    def __init__(self):
        pass  # TODO: initialize your data structures here

    # -- Level 1 --------------------------------------------------

    def add_score(self, game, player, score):
        """Add a score for the player in the given game."""
        # TODO: implement
        pass

    def get_top_score(self, game, player):
        """Return the highest score for the player in the game, or None."""
        # TODO: implement
        pass

    def remove_player(self, game, player):
        """Remove all scores for the player in the game."""
        # TODO: implement
        pass

    # -- Level 2 --------------------------------------------------

    def get_top_players(self, game, n):
        """Return top N players as list of 'player:score' strings."""
        # TODO: implement
        pass

    def get_player_rank(self, game, player):
        """Return 1-based rank of the player, or None."""
        # TODO: implement
        pass

    # -- Level 3 --------------------------------------------------

    def add_score_at(self, timestamp, game, player, score, ttl=None):
        """Add a score with timestamp. Optional ttl in seconds."""
        # TODO: implement
        pass

    def get_top_score_at(self, timestamp, game, player):
        """Get top score at a given timestamp, excluding expired scores."""
        # TODO: implement
        pass

    def remove_player_at(self, timestamp, game, player):
        """Remove player at a given timestamp."""
        # TODO: implement
        pass

    def get_top_players_at(self, timestamp, game, n):
        """Get top N players at a given timestamp, excluding expired scores."""
        # TODO: implement
        pass

    def get_player_rank_at(self, timestamp, game, player):
        """Get player rank at a given timestamp, excluding expired scores."""
        # TODO: implement
        pass

    # -- Level 4 --------------------------------------------------

    def leaderboard_at(self, query_timestamp, game, snapshot_timestamp, n):
        """Return top N players as the leaderboard appeared at snapshot_timestamp."""
        # TODO: implement
        pass


def simulate_coding_framework(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """
    board = Leaderboard()
    results = []

    for command in list_of_lists:
        op = command[0]

        if op == "ADD_SCORE":
            board.add_score(command[1], command[2], int(command[3]))
            results.append(f"added {command[2]} {command[3]}")

        elif op == "GET_TOP_SCORE":
            val = board.get_top_score(command[1], command[2])
            if val is not None:
                results.append(f"top {command[2]} {val}")
            else:
                results.append("not found")

        elif op == "REMOVE_PLAYER":
            board.remove_player(command[1], command[2])
            results.append(f"removed {command[2]}")

        elif op == "GET_TOP_PLAYERS":
            found = board.get_top_players(command[1], int(command[2])) or []
            results.append(f"top players [{', '.join(found)}]")

        elif op == "GET_PLAYER_RANK":
            val = board.get_player_rank(command[1], command[2])
            if val is not None:
                results.append(f"rank {command[2]} {val}")
            else:
                results.append("not found")

        elif op == "ADD_SCORE_AT":
            ttl = int(command[5]) if len(command) > 5 else None
            board.add_score_at(command[1], command[2], command[3], int(command[4]), ttl)
            results.append(f"added at {command[3]} {command[4]}")

        elif op == "GET_TOP_SCORE_AT":
            val = board.get_top_score_at(command[1], command[2], command[3])
            if val is not None:
                results.append(f"top at {command[3]} {val}")
            else:
                results.append("not found")

        elif op == "REMOVE_PLAYER_AT":
            board.remove_player_at(command[1], command[2], command[3])
            results.append(f"removed at {command[3]}")

        elif op == "GET_TOP_PLAYERS_AT":
            found = board.get_top_players_at(command[1], command[2], int(command[3])) or []
            results.append(f"top players at [{', '.join(found)}]")

        elif op == "GET_PLAYER_RANK_AT":
            val = board.get_player_rank_at(command[1], command[2], command[3])
            if val is not None:
                results.append(f"rank at {command[3]} {val}")
            else:
                results.append("not found")

        elif op == "LEADERBOARD_AT":
            found = board.leaderboard_at(command[1], command[2], command[3], int(command[4])) or []
            results.append(f"leaderboard at [{', '.join(found)}]")

    return results
