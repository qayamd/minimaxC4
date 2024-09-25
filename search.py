from node import Connect4Node
from typing import Tuple

def minimax(node: Connect4Node, depth: int, alpha: float, beta: float, maximizing_player: bool) -> Tuple[int, Connect4Node]:
    if depth == 0 or node.is_terminal():
        return node.evaluate(), node

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for child in node.get_children():
            eval, _ = minimax(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for child in node.get_children():
            eval, _ = minimax(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_best_move(node: Connect4Node, depth: int = 7) -> Connect4Node:
    _, best_move = minimax(node, depth, float('-inf'), float('inf'), True)
    return best_move