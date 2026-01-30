import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict


class EventScheduler:
    def __init__(self):
        pass  # TODO: initialize your data structures here

    # -- Level 1 --------------------------------------------------

    def create_event(self, event_id, start_time, end_time, user=None):
        """Create an event. Returns True if created, False if conflict."""
        # TODO: implement
        pass

    def get_event(self, event_id):
        """Return (start_time, end_time) for the event, or None."""
        # TODO: implement
        pass

    def delete_event(self, event_id):
        """Delete the event. Does nothing if not found."""
        # TODO: implement
        pass

    # -- Level 2 --------------------------------------------------

    def events_in_range(self, range_start, range_end):
        """Return list of event_ids overlapping with the range, sorted by start_time then event_id."""
        # TODO: implement
        pass

    def next_event(self, after_time):
        """Return the event_id of the next event starting strictly after after_time, or None."""
        # TODO: implement
        pass

    # -- Level 3 --------------------------------------------------

    def create_recurring(self, event_id, start_time, end_time, interval, user=None):
        """Create a recurring event repeating every interval time units."""
        # TODO: implement
        pass

    def get_occurrences(self, event_id, range_start, range_end):
        """Return list of (start, end) tuples for all occurrences overlapping the range."""
        # TODO: implement
        pass

    # -- Level 4 --------------------------------------------------

    def user_schedule(self, user, range_start, range_end):
        """Return list of (event_id, start, end) for all occurrences in range for the user."""
        # TODO: implement
        pass

    def find_free_time(self, user, range_start, range_end, duration):
        """Return (free_start, free_end) of the earliest available slot, or None."""
        # TODO: implement
        pass


def simulate_coding_framework(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """
    scheduler = EventScheduler()
    results = []

    for command in list_of_lists:
        op = command[0]

        if op == "CREATE_EVENT":
            user = command[4] if len(command) > 4 else None
            created = scheduler.create_event(command[1], int(command[2]), int(command[3]), user)
            if created:
                results.append(f"created {command[1]}")
            else:
                results.append(f"conflict {command[1]}")

        elif op == "GET_EVENT":
            val = scheduler.get_event(command[1])
            if val is not None:
                results.append(f"event {command[1]} {val[0]} {val[1]}")
            else:
                results.append("not found")

        elif op == "DELETE_EVENT":
            scheduler.delete_event(command[1])
            results.append(f"deleted {command[1]}")

        elif op == "EVENTS_IN_RANGE":
            found = scheduler.events_in_range(int(command[1]), int(command[2])) or []
            results.append(f"events [{', '.join(found)}]")

        elif op == "NEXT_EVENT":
            val = scheduler.next_event(int(command[1]))
            if val is not None:
                results.append(f"next {val}")
            else:
                results.append("none")

        elif op == "CREATE_RECURRING":
            user = command[5] if len(command) > 5 else None
            created = scheduler.create_recurring(command[1], int(command[2]), int(command[3]), int(command[4]), user)
            if created:
                results.append(f"created {command[1]}")
            else:
                results.append(f"conflict {command[1]}")

        elif op == "GET_OCCURRENCES":
            found = scheduler.get_occurrences(command[1], int(command[2]), int(command[3])) or []
            formatted = [f"{s}-{e}" for s, e in found]
            results.append(f"occurrences [{', '.join(formatted)}]")

        elif op == "USER_SCHEDULE":
            found = scheduler.user_schedule(command[1], int(command[2]), int(command[3])) or []
            formatted = [f"{eid}:{s}-{e}" for eid, s, e in found]
            results.append(f"schedule [{', '.join(formatted)}]")

        elif op == "FIND_FREE_TIME":
            val = scheduler.find_free_time(command[1], int(command[2]), int(command[3]), int(command[4]))
            if val is not None:
                results.append(f"free {val[0]}-{val[1]}")
            else:
                results.append("no availability")

    return results
