# Task 3 - Tic-Tac-Toe Minimax AI

A Python-based Tic-Tac-Toe game where a human player competes against an AI player using the Minimax algorithm.

## Overview

This project implements a classic 3×3 Tic-Tac-Toe game in Python.

The human player plays as **X**, while the computer plays as **O**.

The AI uses the **Minimax algorithm** to explore possible future game states and select the best available move based on the possible outcomes.

## How It Works

The game follows this flow:

```text
Human Player
     |
     v
Enter Move
     |
     v
Validate Move
     |
     v
Place X
     |
     v
Check Winner / Draw
     |
     v
AI Calculates Best Move
     |
     v
Minimax Algorithm
     |
     v
Explore Future States
     |
     v
Select Best Move
     |
     v
Place O
     |
     v
Continue Game
```

## Board Representation

The board initially contains numbers from 1 to 9:

```text
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

The numbers represent empty cells.

When a player makes a move, the corresponding number is replaced by their symbol.

Example:

```text
['X', 2, 3]
[4, 'O', 6]
[7, 8, 9]
```

## Players

```text
Human Player → X
AI Player    → O
```

## Minimax Algorithm

The AI uses the **Minimax algorithm** to evaluate possible future game states.

The algorithm recursively explores possible moves until it reaches a terminal state.

The evaluation scores are:

```text
O wins → +1
Draw   →  0
X wins → -1
```

The scores are calculated from the AI's perspective.

Therefore:

```text
O → Maximizing Player
X → Minimizing Player
```

### Maximizing Player

When it is O's turn, the algorithm selects the highest score:

```python
best_score = max(best_score, score)
```

### Minimizing Player

When it is X's turn, the algorithm selects the lowest score:

```python
best_score = min(best_score, score)
```

## Recursive Game Simulation

For every available move, the algorithm temporarily places the current player's symbol:

```python
grid[i][j] = player
```

It then switches the turn to the other player and recursively calls Minimax:

```python
score = minimax(grid, other_player)
```

After evaluating the hypothetical move, the board is restored:

```python
grid[i][j] = move
```

This allows the algorithm to evaluate multiple possible moves without permanently changing the actual board.

## Score Propagation

When Minimax reaches a terminal state, it returns one of three scores:

```text
O wins → +1
Draw   →  0
X wins → -1
```

These scores are propagated back through the recursion tree.

For example:

```text
                O
              /   \
             X     X
            / \   / \
           +1 0  -1  0
```

The X nodes minimize the score, while the O nodes maximize the score.

## Optimal Move Selection

The `optimal_decision()` function evaluates every available move for the AI.

For each possible O move:

```python
grid[i][j] = 'O'
score = minimax(grid, "X")
grid[i][j] = move
```

The move with the highest score is selected.

For example:

```text
Move 3 → -1
Move 4 →  0
Move 5 → +1
Move 6 →  0
```

The AI selects **Move 5** because it provides the highest score.

## Main Functions

### `print_board()`

Displays the current Tic-Tac-Toe board.

### `check_winner()`

Checks all rows, columns, and diagonals to determine whether a player has won.

### `is_draw()`

Checks whether the board is full without a winner.

### `get_empty_cells()`

Returns all currently available moves.

### `minimax()`

Recursively explores future game states and calculates the best possible score.

### `optimal_decision()`

Evaluates possible AI moves and selects the move with the highest Minimax score.

## Example Gameplay

```text
Enter your move1

User Moves ...

['X', 2, 3]
[4, 5, 6]
[7, 8, 9]

AI moves ....

['X', 2, 3]
[4, 'O', 6]
[7, 8, 9]
```

The AI evaluates the available moves using Minimax and selects its move.

The game can end with:

```text
X(Player Wins)
```

or:

```text
O(Machine Wins)
```

or:

```text
Draw
```

## Project Structure

```text
Tic-Tac-Toe/
│
├── tic_tac_toe.py
└── README.md
```

### `tic_tac_toe.py`

Contains the complete Tic-Tac-Toe game implementation and Minimax-based AI.

### `README.md`

Contains the project documentation.

## Technologies Used

* Python
* Recursion
* Minimax Algorithm
* Basic Data Structures

## Learning Outcomes

This project demonstrates:

* Python programming
* Functions and modular programming
* Nested loops
* Recursion
* Game-state representation
* Terminal-state evaluation
* Minimax algorithm
* MAX and MIN decision making
* Temporary state modification and restoration
* AI-based decision making

## Limitations

This implementation is designed for a standard 3×3 Tic-Tac-Toe board.

Minimax can efficiently explore the relatively small state space of Tic-Tac-Toe. For larger games, techniques such as **Alpha-Beta Pruning**, depth limiting, and heuristic evaluation can be used to improve efficiency.

## Conclusion

This project demonstrates how a simple game-playing AI can be implemented using the Minimax algorithm.

Instead of selecting moves randomly, the AI evaluates possible future states, considers the opponent's possible responses, and selects the move with the best possible outcome from its perspective.

## Author

**Syed Kaysan Ul Islam**

B.Tech in Artificial Intelligence & Machine Learning
