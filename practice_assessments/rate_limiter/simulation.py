import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict


class RateLimiter:
    def __init__(self):
        pass  # TODO: initialize your data structures here

    # -- Level 1 --------------------------------------------------

    def allow_request(self, user, endpoint):
        """Record a request. At this level, always returns 'allowed'."""
        # TODO: implement
        pass

    def get_request_count(self, user):
        """Return total request count for user across all endpoints."""
        # TODO: implement
        pass

    def clear_user(self, user):
        """Clear all recorded requests for the user."""
        # TODO: implement
        pass

    # -- Level 2 --------------------------------------------------

    def set_limit(self, endpoint, max_requests):
        """Set a rate limit for the endpoint (max requests per user)."""
        # TODO: implement
        pass

    def get_endpoint_count(self, user, endpoint):
        """Return request count for user on specific endpoint."""
        # TODO: implement
        pass

    # -- Level 3 --------------------------------------------------

    def set_limit_at(self, timestamp, endpoint, max_requests, window):
        """Set a rate limit with a time window in seconds."""
        # TODO: implement
        pass

    def allow_request_at(self, timestamp, user, endpoint):
        """Record a request at timestamp. Check window-based limit."""
        # TODO: implement
        pass

    def get_request_count_at(self, timestamp, user):
        """Count non-expired requests for user across all endpoints."""
        # TODO: implement
        pass

    def get_endpoint_count_at(self, timestamp, user, endpoint):
        """Count non-expired requests for user on specific endpoint."""
        # TODO: implement
        pass

    # -- Level 4 --------------------------------------------------

    def rate_limit_status_at(self, query_timestamp, user, endpoint, snapshot_timestamp):
        """Return rate limit status at snapshot_timestamp as 'X/Y' or 'X/unlimited'."""
        # TODO: implement
        pass


def simulate_coding_framework(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """
    limiter = RateLimiter()
    results = []

    for command in list_of_lists:
        op = command[0]

        if op == "ALLOW_REQUEST":
            val = limiter.allow_request(command[1], command[2])
            results.append(val if val else "allowed")

        elif op == "GET_REQUEST_COUNT":
            val = limiter.get_request_count(command[1])
            results.append(f"count {val if val is not None else 0}")

        elif op == "CLEAR_USER":
            limiter.clear_user(command[1])
            results.append(f"cleared {command[1]}")

        elif op == "SET_LIMIT":
            limiter.set_limit(command[1], int(command[2]))
            results.append(f"limit set {command[1]} {command[2]}")

        elif op == "GET_ENDPOINT_COUNT":
            val = limiter.get_endpoint_count(command[1], command[2])
            results.append(f"count {val if val is not None else 0}")

        elif op == "SET_LIMIT_AT":
            limiter.set_limit_at(int(command[1]), command[2], int(command[3]), int(command[4]))
            results.append(f"limit set {command[2]} {command[3]} {command[4]}")

        elif op == "ALLOW_REQUEST_AT":
            val = limiter.allow_request_at(int(command[1]), command[2], command[3])
            results.append(val if val else "allowed")

        elif op == "GET_REQUEST_COUNT_AT":
            val = limiter.get_request_count_at(int(command[1]), command[2])
            results.append(f"count {val if val is not None else 0}")

        elif op == "GET_ENDPOINT_COUNT_AT":
            val = limiter.get_endpoint_count_at(int(command[1]), command[2], command[3])
            results.append(f"count {val if val is not None else 0}")

        elif op == "RATE_LIMIT_STATUS_AT":
            val = limiter.rate_limit_status_at(int(command[1]), command[2], command[3], int(command[4]))
            results.append(val if val else "0/unlimited")

    return results
