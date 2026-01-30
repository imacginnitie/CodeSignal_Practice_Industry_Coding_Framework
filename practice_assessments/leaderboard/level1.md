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
