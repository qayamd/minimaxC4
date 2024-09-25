# Connect 4 AI

## What is it?
This repo contains an implementation of a Connect 4 game with an AI opponent using the Minimax algorithm with alpha-beta pruning. The game is implemented in Python using Pygame for the graphical interface.

## How does the AI work?
The AI uses the Minimax algorithm with alpha-beta pruning to make decisions. This approach allows the AI to look ahead several moves and choose the best possible move based on the current game state.

### Minimax Algorithm
The Minimax algorithm is a decision-making algorithm used in two-player turn-based games. It works by recursively evaluating all possible moves and their outcomes, assuming that both players play optimally. The algorithm can be visualized as a tree:

```
       Max
    /   |   \
  Min  Min  Min
 / | \
Max Max Max
```

In our implementation, the AI (Max player) tries to maximize its score, while assuming the human player (Min player) will try to minimize the AI's score.

### Alpha-Beta Pruning
To improve the efficiency of the Minimax algorithm, we use alpha-beta pruning. This technique allows us to eliminate branches of the search tree that don't need to be explored, significantly reducing the number of nodes evaluated.

## Why is it efficient?
The combination of Minimax and alpha-beta pruning provides an efficient way to search through the game tree:

1. **Reduced search space**: Alpha-beta pruning allows the algorithm to ignore branches that are guaranteed to be worse than already explored options.
2. **Depth-limited search**: By limiting the search depth, we can balance between decision quality and computation time.
3. **Efficient pruning**: The ordering of moves based on the heuristic evaluation helps to prune more branches earlier in the search.

## Heuristic Evaluation
The heuristic function is crucial for evaluating non-terminal game states. Our heuristic considers the following factors:

1. **Winning positions**: Highest priority is given to winning moves.
2. **Blocking opponent wins**: High priority is given to moves that prevent the opponent from winning.
3. **Potential connections**: The heuristic evaluates all possible 4-in-a-row combinations, giving scores based on the number of AI and opponent pieces in each window.

Here's how the heuristic is implemented:

```python
def heuristic(self) -> int:
    score = 0
    
    # Check all possible 4-in-a-row combinations
    for row in range(6):
        for col in range(7):
            # Horizontal, Vertical, and Diagonal checks
            # ...

    return score

def evaluate_window(self, window: List[int]) -> int:
    score = 0
    ai_count = window.count(2)
    human_count = window.count(1)
    empty_count = window.count(0)

    if ai_count == 4:
        score += 100
    elif ai_count == 3 and empty_count == 1:
        score += 5
    elif ai_count == 2 and empty_count == 2:
        score += 2

    if human_count == 3 and empty_count == 1:
        score -= 4

    return score
```

This heuristic allows the AI to make informed decisions even when it can't see all the way to the end of the game.

## When is it more efficient?
The efficiency of the AI depends on several factors:

1. **Board state**: In the early game, with many possible moves, the alpha-beta pruning is particularly effective at reducing the search space.
2. **Search depth**: Deeper searches provide better play but take more time. The current implementation uses a depth of 7, which provides a good balance between speed and play quality.
3. **Move ordering**: The effectiveness of alpha-beta pruning is improved by evaluating the most promising moves first, which our heuristic helps to achieve.

## What does what?
* `environment.py`: Contains the main game logic and Pygame interface.
* `node.py`: Implements the Connect4Node class, which represents game states and includes the heuristic evaluation.
* `search.py`: Contains the Minimax algorithm with alpha-beta pruning.

To run the game, execute `python environment.py` from the command line. Enjoy playing against the AI!