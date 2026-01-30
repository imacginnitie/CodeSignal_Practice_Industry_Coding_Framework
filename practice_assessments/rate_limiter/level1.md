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
