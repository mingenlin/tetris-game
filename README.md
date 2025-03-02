# Tetris Game

This is a simple implementation of the classic Tetris game using Python and Pygame. The game allows players to control falling tetrominoes, clearing lines and scoring points.

## Project Structure

```
tetris-game
├── src
│   ├── tetris.py       # Initializes Pygame, sets up the game loop and rendering
│   ├── game.py         # Contains the main game logic and state management
│   └── utils.py        # Provides utility functions for game operations
├── requirements.txt     # Lists the dependencies required to run the project
└── README.md            # Documentation for the project
```

## Requirements

To run this project, you need to have Python and Pygame installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Game

To start the game, run the following command in your terminal:

```
python src/tetris.py
```

## Controls

- **Left Arrow**: Move the tetromino left
- **Right Arrow**: Move the tetromino right
- **Down Arrow**: Move the tetromino down
- **Up Arrow**: Rotate the tetromino
- **Space**: Drop the tetromino to the bottom

## Features

- Classic Tetris gameplay
- Scoring system based on cleared lines
- Game over condition when pieces stack to the top

Enjoy playing Tetris!