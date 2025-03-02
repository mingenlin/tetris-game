import random
import pygame

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

class TetrisGame:
    def __init__(self):
        self.board = self._create_board()
        self.current_piece = self._new_piece()
        self.piece_x = 3  # Initial x position of the piece
        self.piece_y = 0  # Initial y position of the piece
        self.lines_cleared = 0  # Initialize lines cleared
        self.game_over = False

    def _create_board(self):
        return [[0 for _ in range(10)] for _ in range(20)]

    def _new_piece(self):
        # Generate a new Tetris piece
        return random.choice(SHAPES)

    def rotate(self):
        # Rotate the current piece
        self.current_piece = [list(row) for row in zip(*self.current_piece[::-1])]

    def move(self, direction):
        # Move the current piece left, right, or down
        if direction == 'left':
            self.piece_x -= 1
            if self._check_collision():
                self.piece_x += 1
        elif direction == 'right':
            self.piece_x += 1
            if self._check_collision():
                self.piece_x -= 1
        elif direction == 'down':
            self.piece_y += 1
            if self._check_collision():
                self.piece_y -= 1
                self._lock_piece()
                self.current_piece = self._new_piece()
                self.piece_x = 3
                self.piece_y = 0
                if self._check_collision():
                    self.game_over = True

    def drop_piece(self):
        # Drop the current piece to the bottom
        while not self._check_collision():
            self.piece_y += 1
        self.piece_y -= 1
        self._lock_piece()
        self.current_piece = self._new_piece()
        self.piece_x = 3
        self.piece_y = 0
        if self._check_collision():
            self.game_over = True

    def clear_lines(self):
        # Check for completed lines and clear them
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = len(self.board) - len(new_board)
        self.board = [[0 for _ in range(10)] for _ in range(lines_cleared)] + new_board
        self.lines_cleared += lines_cleared  # Increment lines cleared        

    def _check_collision(self):
        # Check for collision with the board or other pieces
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    if (x + self.piece_x < 0 or x + self.piece_x >= len(self.board[0]) or
                        y + self.piece_y < 0 or y + self.piece_y >= len(self.board) or
                        self.board[y + self.piece_y][x + self.piece_x]):
                        return True
        return False

    def _lock_piece(self):
        # Lock the current piece into the board
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    if 0 <= y + self.piece_y < len(self.board) and 0 <= x + self.piece_x < len(self.board[0]):
                        self.board[y + self.piece_y][x + self.piece_x] = cell
        self.clear_lines()

    def check_game_over(self):
        # Check if the game is over
        return self.game_over

    def update(self):
        # Update the game state
        if not self.game_over:
            self.move('down')
            self.clear_lines()

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Draw the board
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * 30, y * 30, 30, 30))

        # Draw the current piece
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((x + self.piece_x) * 30, (y + self.piece_y) * 30, 30, 30))

        # Draw the score and lines cleared
        font = pygame.font.SysFont(None, 36)
        lines_text = font.render(f'Lines: {self.lines_cleared}', True, (255, 255, 255))
        screen.blit(lines_text, (10, 50))

        pygame.display.flip()  # Update the display