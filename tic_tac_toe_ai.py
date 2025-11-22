import math

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.human = "X"
        self.ai = "O"

    def display_board(self):
        print()
        for i in range(3):
            print(" | ".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("--+---+--")
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def winner(self, player):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def full_board(self):
        return " " not in self.board

    def minimax(self, is_maximizing):
        if self.winner(self.ai):
            return 1
        if self.winner(self.human):
            return -1
        if self.full_board():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in self.available_moves():
                self.board[i] = self.ai
                score = self.minimax(False)
                self.board[i] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in self.available_moves():
                self.board[i] = self.human
                score = self.minimax(True)
                self.board[i] = " "
                best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -math.inf
        move = 0
        for i in self.available_moves():
            self.board[i] = self.ai
            score = self.minimax(False)
            self.board[i] = " "
            if score > best_score:
                best_score = score
                move = i
        self.board[move] = self.ai

    def human_move(self):
        while True:
            move = int(input("Enter position (1-9): ")) - 1
            if move in self.available_moves():
                self.board[move] = self.human
                break
            else:
                print("Invalid move, try again.")

    def play(self):
        print("TIC TAC TOE - HUMAN vs AI")
        self.display_board()

        while True:
            self.human_move()
            self.display_board()
            if self.winner(self.human):
                print("You Win!")
                break
            if self.full_board():
                print("Draw!")
                break

            print("AI is thinking...")
            self.ai_move()
            self.display_board()
            if self.winner(self.ai):
                print("AI Wins!")
                break
            if self.full_board():
                print("Draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
