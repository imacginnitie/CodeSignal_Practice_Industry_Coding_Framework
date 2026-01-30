import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

import numpy
import sortedcontainers


class FileStorage:
    def __init__(self):
        pass  # TODO: initialize your data structures here

    # ── Level 1 ──────────────────────────────────────────────

    def file_upload(self, file_name, size):
        """Upload a file. Raises if file already exists."""
        # TODO: implement
        pass

    def file_get(self, file_name):
        """Return the size of the file, or None if it doesn't exist."""
        # TODO: implement
        pass

    def file_copy(self, source, dest):
        """Copy source to dest. Raises if source doesn't exist. Overwrites dest if it exists."""
        # TODO: implement
        pass

    # ── Level 2 ──────────────────────────────────────────────

    def file_search(self, prefix):
        """Find top 10 files matching prefix, sorted by size desc then name asc."""
        # TODO: implement
        pass

    # ── Level 3 ──────────────────────────────────────────────

    def file_upload_at(self, timestamp, file_name, size, ttl=None):
        """Upload with timestamp. Optional ttl in seconds."""
        # TODO: implement
        pass

    def file_get_at(self, timestamp, file_name):
        """Get file at a given timestamp. Returns None if expired or missing."""
        # TODO: implement
        pass

    def file_copy_at(self, timestamp, source, dest):
        """Copy file at a given timestamp."""
        # TODO: implement
        pass

    def file_search_at(self, timestamp, prefix):
        """Search for files at a given timestamp, excluding expired files."""
        # TODO: implement
        pass

    # ── Level 4 ──────────────────────────────────────────────

    def rollback(self, timestamp):
        """Rollback file storage state to the given timestamp."""
        # TODO: implement
        pass


def simulate_coding_framework(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """
    storage = FileStorage()
    results = []

    for command in list_of_lists:
        op = command[0]

        if op == "FILE_UPLOAD":
            storage.file_upload(command[1], command[2])
            results.append(f"uploaded {command[1]}")

        elif op == "FILE_GET":
            val = storage.file_get(command[1])
            if val is not None:
                results.append(f"got {command[1]}")
            else:
                results.append("file not found")

        elif op == "FILE_COPY":
            storage.file_copy(command[1], command[2])
            results.append(f"copied {command[1]} to {command[2]}")

        elif op == "FILE_SEARCH":
            found = storage.file_search(command[1])
            results.append(f"found [{', '.join(found)}]")

        elif op == "FILE_UPLOAD_AT":
            ttl = int(command[4]) if len(command) > 4 else None
            storage.file_upload_at(command[1], command[2], command[3], ttl)
            results.append(f"uploaded at {command[2]}")

        elif op == "FILE_GET_AT":
            val = storage.file_get_at(command[1], command[2])
            if val is not None:
                results.append(f"got at {command[2]}")
            else:
                results.append("file not found")

        elif op == "FILE_COPY_AT":
            storage.file_copy_at(command[1], command[2], command[3])
            results.append(f"copied at {command[2]} to {command[3]}")

        elif op == "FILE_SEARCH_AT":
            found = storage.file_search_at(command[1], command[2])
            results.append(f"found at [{', '.join(found)}]")

        elif op == "ROLLBACK":
            storage.rollback(command[1])
            results.append(f"rollback to {command[1]}")

    return results
