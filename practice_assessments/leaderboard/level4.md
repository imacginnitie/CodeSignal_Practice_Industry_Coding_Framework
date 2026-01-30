# Scenario

Your task is to implement a simplified version of a gaming leaderboard system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of a leaderboard with various games and players:

```plaintext
[Game: SpaceRace]
    Player       Score
    +- alice      1500
    +- alice      1200
    +- bob        1800
    +- charlie    1500

[Game: PuzzleQuest]
    Player       Score
    +- alice      900
    +- bob        750
```

## Level 1 -- Initial Design & Basic Functions

- **ADD_SCORE(game, player, score)**
  - Add a score for the player in the given game. A player can have multiple scores in the same game.
- **GET_TOP_SCORE(game, player)**
  - Return the highest score for the player in the given game, or nothing if the player has no scores in that game.
- **REMOVE_PLAYER(game, player)**
  - Remove all scores for the player in the given game. Does nothing if the player has no scores.

## Level 2 -- Data Structures & Data Processing

- **GET_TOP_PLAYERS(game, n)**
  - Return the top N players for a game, ranked by their highest score in descending order. In case of a tie, order by player name in ascending alphabetical order. Each entry in the result is formatted as "player:score".
- **GET_PLAYER_RANK(game, player)**
  - Return the 1-based rank of the player in the game based on their highest score. If two players have the same top score, the one with the alphabetically earlier name gets the lower (better) rank. Returns nothing if the player has no scores in the game.

## Level 3 -- Refactoring & Encapsulation

Scores now have timestamps and may have a time to live (TTL). Implement extensions of existing methods which inherit all functionality but also include a timestamp parameter. Scores with a TTL expire after that many seconds from the timestamp at which they were added. No TTL means the score lives forever.

- **ADD_SCORE_AT(timestamp, game, player, score)**
- **ADD_SCORE_AT(timestamp, game, player, score, ttl)**
  - The score is available for ttl seconds from the given timestamp.
- **GET_TOP_SCORE_AT(timestamp, game, player)**
  - Only considers scores that have not expired at the given timestamp.
- **REMOVE_PLAYER_AT(timestamp, game, player)**
- **GET_TOP_PLAYERS_AT(timestamp, game, n)**
  - Only considers scores that have not expired at the given timestamp.
- **GET_PLAYER_RANK_AT(timestamp, game, player)**
  - Only considers scores that have not expired at the given timestamp.

## Level 4 -- Extending Design & Functionality

- **LEADERBOARD_AT(query_timestamp, game, snapshot_timestamp, n)**
  - Return the top N players for the game as the leaderboard would have appeared at snapshot_timestamp. Only scores that were added at or before snapshot_timestamp and had not expired by snapshot_timestamp should be considered. Player removals that occurred at or before snapshot_timestamp should also be reflected. Ranking rules are the same as GET_TOP_PLAYERS.
