# Scenario

Your task is to implement a simplified version of an API rate limiter system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of a rate limiter tracking API requests per user:

```plaintext
[User: alice]
    Endpoint           Count
    +- /api/data        2
    +- /api/users       1

[User: bob]
    Endpoint           Count
    +- /api/data        1
```

## Level 1 -- Initial Design & Basic Operations

- **ALLOW_REQUEST(user, endpoint)**
  - Record a request from the user to the given endpoint. At this level, all requests are always allowed. Returns "allowed".
- **GET_REQUEST_COUNT(user)**
  - Return the total number of requests the user has made across all endpoints. Returns "0" if the user has no recorded requests.
- **CLEAR_USER(user)**
  - Clear all recorded requests for the given user. Does nothing if the user has no requests.

## Level 2 -- Rate Limiting

- **SET_LIMIT(endpoint, max_requests)**
  - Set a rate limit for the given endpoint. Each user may make at most max_requests requests to this endpoint. If a limit was previously set, it is overwritten.
- **ALLOW_REQUEST(user, endpoint)**
  - Now checks whether the user has reached the rate limit for the endpoint. If the user's request count for this endpoint equals or exceeds max_requests, the request is denied and not recorded. Returns "allowed" or "denied". If no limit has been set for the endpoint, the request is always allowed.
- **GET_ENDPOINT_COUNT(user, endpoint)**
  - Return the number of requests the user has made to the specific endpoint. Returns "0" if none.

## Level 3 -- Time Windows

Rate limits now apply within a sliding time window. All operations gain `_AT` variants that accept integer timestamps. Requests are only counted if they fall within the window.

- **SET_LIMIT_AT(timestamp, endpoint, max_requests, window)**
  - Set a rate limit for the endpoint: at most max_requests per user within a sliding window of window seconds. Overwrites any previous limit for this endpoint.
- **ALLOW_REQUEST_AT(timestamp, user, endpoint)**
  - Record a request at the given timestamp. Only requests within the window (i.e., with timestamps strictly greater than `timestamp - window`) are counted toward the limit. If the count of in-window requests equals or exceeds max_requests, the request is denied and not recorded. Returns "allowed" or "denied". If no limit is set, the request is always allowed and recorded.
- **GET_REQUEST_COUNT_AT(timestamp, user)**
  - Return the total number of non-expired requests for the user across all endpoints. For each endpoint with a limit, only requests within that endpoint's window at the given timestamp are counted. For endpoints without a limit, all requests are counted.
- **GET_ENDPOINT_COUNT_AT(timestamp, user, endpoint)**
  - Return the number of non-expired requests for the user on the specific endpoint. For endpoints with a limit, only requests within the window at the given timestamp are counted. For endpoints without a limit, all requests are counted.

## Level 4 -- Rate Limit History

- **RATE_LIMIT_STATUS_AT(query_timestamp, user, endpoint, snapshot_timestamp)**
  - Return what the user's rate limit status would have been at snapshot_timestamp for the given endpoint. Count all requests the user made to the endpoint at or before snapshot_timestamp that are within the endpoint's window at snapshot_timestamp (i.e., with timestamps strictly greater than `snapshot_timestamp - window`). The result is formatted as "X/Y" where X is the count and Y is the max_requests limit. If no limit is set for the endpoint, the format is "X/unlimited" where X is the total number of requests at or before snapshot_timestamp.
