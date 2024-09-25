from typing import List, Optional

class Connect4Node:
    def __init__(self, board: Optional[List[List[int]]] = None, player: int = 1):
        self.board = board if board else [[0 for _ in range(7)] for _ in range(6)]
        self.player = player

    def get_valid_moves(self) -> List[int]:
        return [col for col in range(7) if self.board[0][col] == 0]

    def make_move(self, column: int) -> Optional['Connect4Node']:
        if column not in self.get_valid_moves():
            return None
        
        new_board = [row.copy() for row in self.board]
        for row in range(5, -1, -1):
            if new_board[row][column] == 0:
                new_board[row][column] = self.player
                break
        
        return Connect4Node(new_board, 3 - self.player)  # Switch player (1 -> 2, 2 -> 1)

    def is_winner(self, player: int) -> bool:
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col+i] == player for i in range(4)):
                    return True
        
        # Check vertical
        for row in range(3):
            for col in range(7):
                if all(self.board[row+i][col] == player for i in range(4)):
                    return True
        
        # Check diagonal (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if all(self.board[row+i][col+i] == player for i in range(4)):
                    return True
        
        # Check diagonal (top-right to bottom-left)
        for row in range(3):
            for col in range(3, 7):
                if all(self.board[row+i][col-i] == player for i in range(4)):
                    return True
        
        return False

    def is_terminal(self) -> bool:
        return self.is_winner(1) or self.is_winner(2) or len(self.get_valid_moves()) == 0

    def get_children(self) -> List['Connect4Node']:
        return [self.make_move(col) for col in self.get_valid_moves()]

    def evaluate(self) -> int:
        if self.is_winner(2):
            return 1000000
        elif self.is_winner(1):
            return -1000000
        else:
            return self.heuristic()

    def heuristic(self) -> int:
        score = 0
        
        # Check all possible 4-in-a-row combinations
        for row in range(6):
            for col in range(7):
                # Horizontal
                if col <= 3:
                    window = [self.board[row][col+i] for i in range(4)]
                    score += self.evaluate_window(window)
                
                # Vertical
                if row <= 2:
                    window = [self.board[row+i][col] for i in range(4)]
                    score += self.evaluate_window(window)
                
                # Diagonal (top-left to bottom-right)
                if row <= 2 and col <= 3:
                    window = [self.board[row+i][col+i] for i in range(4)]
                    score += self.evaluate_window(window)
                
                # Diagonal (top-right to bottom-left)
                if row <= 2 and col >= 3:
                    window = [self.board[row+i][col-i] for i in range(4)]
                    score += self.evaluate_window(window)
        
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