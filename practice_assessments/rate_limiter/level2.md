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
