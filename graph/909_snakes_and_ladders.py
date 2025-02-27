from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        length = len(board)
        board.reverse()
        visited = set()  # Keep track of visited squares

        def square_to_position(square):
            # Helper function to take a square and return board position
            row = (square - 1) // length
            col = (square - 1) % length
            # Every second row is flipped
            if row % 2:
                col = length - col - 1
            return row, col

        # Use a queue to keep track of squares to move from and moves made
        # Initialize with square 1, zero moves
        q = deque([(1, 0)])  # [Square, moves to get there]

        # Perform bfs on queue
        while q:
            # Get next square, moves
            square, moves = q.popleft()
            # Simulate dice rolls
            for roll in range(1, 7):
                next_square = square + roll
                # Get grid position
                row, col = square_to_position(next_square)
                # Check if snake or ladder and move
                if board[row][col] != -1:
                    next_square = board[row][col]
                # Check if we have reach the end of the board
                if next_square == length ** 2:
                    return moves + 1
                # If we have not visited square, add to moves queue
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, moves + 1])
        
        # If we have emptied the queue then it is impossible to reach the end of the board
        return -1