import pygame
import sys
from node import Connect4Node
from search import get_best_move

class Connect4Game:
    def __init__(self):
        pygame.init()
        self.width = 700
        self.height = 600
        self.cell_size = 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Connect 4')
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.current_node = Connect4Node()
        self.game_over = False
        self.winner = None

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for col in range(7):
            for row in range(6):
                pygame.draw.rect(self.screen, (0, 0, 255), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.circle(self.screen, (255, 255, 255), (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

        for col in range(7):
            for row in range(6):
                if self.current_node.board[row][col] == 1:
                    color = (255, 0, 0)  # Red for player 1
                elif self.current_node.board[row][col] == 2:
                    color = (255, 255, 0)  # Yellow for player 2
                else:
                    continue
                pygame.draw.circle(self.screen, color, (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 5)

    def handle_click(self, pos):
        if self.game_over or self.current_node.player != 1:
            return

        col = pos[0] // self.cell_size
        new_node = self.current_node.make_move(col)
        if new_node:
            self.current_node = new_node
            self.check_game_over()
            
        if not self.game_over:
            ai_move = get_best_move(self.current_node)
            self.current_node = ai_move
            self.check_game_over()

    def check_game_over(self):
        if self.current_node.is_terminal():
            self.game_over = True
            if self.current_node.is_winner(1):
                self.winner = 1
            elif self.current_node.is_winner(2):
                self.winner = 2

    def display_winner(self):
        if self.winner:
            text = f"Player {self.winner} wins!"
        else:
            text = "It's a draw!"
        text_surface = self.font.render(text, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text_surface, text_rect)

        restart_text = self.small_font.render("Click to play again", True, (0, 0, 0))
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height - 50))
        self.screen.blit(restart_text, restart_rect)

    def play(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.handle_click(pygame.mouse.get_pos())

            self.draw_board()
            if self.game_over:
                self.display_winner()

            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    game = Connect4Game()
    game.play()