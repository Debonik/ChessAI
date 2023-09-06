# ChessAI
## `main.py`

**What it does**:  
This is where the game starts and runs. It allows you to play moves and makes the AI take its turn too.

**Key Parts**:  
- Sets up the chess board.
- Manages turns between you and the AI.

---

## `minimax.py`

**What it does**:  
This file helps the AI think about its moves. It looks ahead at possible future board states to decide the best move.

**Key Parts**:  
- Minimax Algorithm: Helps the AI think ahead and evaluate moves.
- Alpha-Beta Pruning: Makes the thinking process faster.

---

## `evaluation.py`

**What it does**:  
This file judges how good or bad a particular board setup is for the AI.

**Key Parts**:  
- Assigns point values to different chess pieces.
- Calculates the total points for the board.

---

## `helper_functions.py`

**What it does**:  
This is like the AI's toolbox. It contains helpful functions to make other tasks easier, like converting the board into different formats.

**Key Parts**:  
- Converts the board to a picture (SVG format).
- Converts the board to a grid (matrix) format.

---

## `reinforcement_learning.py` (Optional)

**What it does**:  
This file helps the AI learn from playing games. It uses a neural network to learn better moves over time.

**Key Parts**:  
- Neural Network: The brain of the AI where learning happens.
- Training Function: Helps the AI learn from each game.
