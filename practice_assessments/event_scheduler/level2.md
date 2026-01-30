# Scenario

Your task is to implement a simplified version of an event scheduling system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of an event schedule with various events on a timeline:

```plaintext
[Timeline]
    Event        Start   End
    +- meeting     10     20
    +- lunch       30     40
    +- workshop    50     60
```

## Level 1 -- Basic Operations

- **CREATE_EVENT(event_id, start_time, end_time)**
  - Create an event with the given time range (integer timestamps). Returns confirmation.
- **GET_EVENT(event_id)**
  - Return the event's details, or nothing if the event does not exist.
- **DELETE_EVENT(event_id)**
  - Delete the event. Does nothing if the event does not exist.

## Level 2 -- Conflict Detection & Querying

- **CREATE_EVENT(event_id, start_time, end_time)**
  - Now rejects if the new event overlaps with any existing event. Two events conflict if their time ranges overlap. Sharing only an endpoint is NOT a conflict (e.g. [1,5] and [5,10] do not conflict). Returns confirmation or conflict notice.
- **EVENTS_IN_RANGE(range_start, range_end)**
  - Return all events that overlap with the given range, sorted by start_time ascending, then event_id ascending. Two intervals overlap when `start1 < end2 AND start2 < end1`.
- **NEXT_EVENT(after_time)**
  - Return the next event starting strictly after the given time. If multiple events share the same earliest qualifying start_time, return the one with the smallest event_id. Returns the event or nothing.
