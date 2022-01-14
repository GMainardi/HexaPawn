from Board import Board
from Players import Human, Random, AI

class Game():

    WHITE = True
    BLACK = False

    def __init__(self, white=0, black=0, board=None, turn = True) -> None:

        if not board:
            self.board = Board()
        else:
            self.board = board

        self.turn = turn

        if white == 0:
            self.white = Human(self.WHITE)
        elif white == 1:
            self.white = AI(self.WHITE)
        elif white == 2:
            from Players import MonteCarlo
            self.white = MonteCarlo(self.WHITE)
        else:
            self.white = Random(self.WHITE)

        if black == 0:
            self.black = Human(self.BLACK)
        elif black == 1:
            self.black = AI(self.BLACK)
        elif black == 2:
            from Players import MonteCarlo
            self.black = MonteCarlo(self.BLACK)
        else:
            self.black = Random(self.BLACK)

        if self.human_playing():
            self.board.help()
        
    def change_player(self, player):
        if player == self.WHITE:
            self.white = Human(self.WHITE)
        else:
            self.black = Human(self.BLACK)
        self.turn = self.WHITE

    def train(self):
        max_games = 1000
        play_another_game = True
        i = 0

        while play_another_game and (max_games-i):
            
            winner = self.run()

            if not self.human_playing() and i % 50 == 0:
                win = 'whites' if winner == self.WHITE else 'blacks'
                print(f'game {i} winner: {win}')

            if type(self.white) == AI and winner != self.WHITE:
                self.white.learn()

            if type(self.black) == AI and winner != self.BLACK:
                self.black.learn()

            if self.human_playing():
                play_another_game = bool(input('if you want to stop play type 1 otherwise type 0:\n'))
            
            i += 1
            
            
            self.board = Board()
        
        if not self.human_playing():
            print('at this point the black AI knows how to win in ever single case do you can beat the black AI?' )

    def run(self):

        end = False
        while not end:

            end = self.play()

            self.turn = not self.turn

            if end == -1:
                self.print(self.board)
                return self.turn
        

        self.print(self.board)
        return not self.turn


    def play(self):

        self.print(self.board)

        if self.turn:
            self.print('whites')
            played = self.white.play(self.board.pieces.copy())
            if not played:
                return -1
        else:
            self.print('blacks')
            played = self.black.play(self.board.pieces.copy())
            if not played:
                return -1
        
        self.captrue()

        return self.end()
        
    def captrue(self):
        for i in range(len(self.board.pieces)):
            p1 = self.board.pieces[i]
            for j in range(i + 1, len(self.board.pieces)):
                p2 = self.board.pieces[j]
                if p1.pos == p2.pos:
                    if p1.white == self.turn:
                        self.board.pieces.remove(p2)
                    else:
                        self.board.pieces.remove(p1)
                    return
    
    def end(self):

        black_moves = 0
        blacks = 0
        white_moves = 0
        whites = 0

        for piece in self.board.pieces:
            if piece.white:
                white_moves += len(piece.moves(self.board.pieces))
                if piece.pos[1] == 2:
                    self.print('White wins!')
                    return True
                whites += 1
            if not piece.white:
                black_moves += len(piece.moves(self.board.pieces))
                if piece.pos[1] == 0:
                    self.print('Blacks wins!')
                    return True
                blacks += 1
        
        if whites == 0 or (not white_moves and not self.turn):
            self.print('Blacks wins!')
            return True

        if blacks == 0 or (not black_moves and self.turn):
            self.print('White wins!')
            return True
        
        return False
        
    def human_playing(self) -> bool:
        return type(self.white) is Human or type(self.black) is Human
    
    def print(self, string):
        if self.human_playing():
            print(string)
