import math

class TicTacToe:
    def __init__(self, board=None):
        self.board = board or [[' ' for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def is_winner(self, player):
        # Проверка строк, столбцов и диагоналей
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
    
    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.is_winner('X'):
            return 10 - depth
        if self.is_winner('O'):
            return depth - 10
        if self.is_full():
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = 'X'
                score = self.minimax(depth + 1, False, alpha, beta)
                self.board[i][j] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = 'O'
                score = self.minimax(depth + 1, True, alpha, beta)
                self.board[i][j] = ' '
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
    
    def find_best_move(self):
        best_score = -math.inf
        best_move = (-1, -1)
        for i, j in self.get_empty_cells():
            self.board[i][j] = 'X'
            score = self.minimax(0, False, -math.inf, math.inf)
            self.board[i][j] = ' '
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_move

# Пример использования
if __name__ == "__main__":
    game = TicTacToe([
        ['X', 'O', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', 'X']
    ])
    
    print("Текущее поле:")
    game.print_board()
    
    move = game.find_best_move()
    print(f"Лучший ход для X: {move}")