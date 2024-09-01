# N-Puzzle Solver with A* Algorithm

## Overview

This project implements a solver for the N-puzzle problem using the A* search algorithm. The N-puzzle is a sliding puzzle that consists of a grid with numbered tiles and one blank space. The goal is to rearrange the tiles to achieve a specified goal configuration.

## Features

- **A* Algorithm**: Utilizes the A* search algorithm to find the optimal solution for the N-puzzle problem.
- **User Input**: Allows users to input the initial and goal configurations of the puzzle.
- **Visualization**: Provides a simple textual representation of the puzzle states.

## How It Works

1. **Node Class**: Represents a state in the puzzle, including its configuration, cost to reach, and heuristic estimate.
2. **Puzzle Class**: Handles the puzzle operations, including generating child nodes, computing costs, and processing the puzzle to find the solution.
3. **Heuristic Function**: Uses a heuristic to estimate the cost from the current state to the goal state.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/n-puzzle-solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd n-puzzle-solver
   ```

### Usage

1. Run the Python script:
   ```bash
   python n_puzzle_solver.py
   ```

2. Enter the initial and goal configurations as prompted.

### Example Input

- **Initial State**:
  ```
  1 2 3
  4 5 6
  7 8 _
  ```

- **Goal State**:
  ```
  1 2 3
  4 5 6
  7 8 _
  ```

### Project Structure

- `n_puzzle_solver.py`: Contains the implementation of the A* algorithm and puzzle solving logic.
- `README.md`: This file, providing an overview and usage instructions.
