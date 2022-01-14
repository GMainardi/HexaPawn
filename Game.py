from Board import Board
import Players


class Game():

    WHITE = True
    BLACK = False

    def __init__(self, white=0, black=0) -> None:

        self.board = Board()

        if white == 0:
            self.white = Players.Human(self.WHITE)
        elif white == 1:
            self.white = Players.AI(self.WHITE)
        else:
            pass

        if black == 0:
            self.black = Players.Human(self.BLACK)
        elif black == 1:
            self.black = Players.AI(self.BLACK)
        else:
            pass

        if self.human_playing():
            self.board.help()
        
    def change_player(self, player):
        if player == self.WHITE:
            self.white = Players.Human(self.WHITE)
        else:
            self.black = Players.Human(self.BLACK)

    def train(self):

        play_another_game = True
        i = 0

        while play_another_game:
            
            winner = self.run()

            if not self.human_playing():
                win = 'whites' if winner == self.WHITE else 'blacks'
                print(f'game {i} winner: {win}')

            if type(self.white) == Players.AI and winner != self.WHITE:
                play_another_game = self.white.learn()

            if type(self.black) == Players.AI and winner != self.BLACK:
                play_another_game = self.black.learn()

            if self.human_playing():
                play_another_game = bool(input('if you want to stop play type 1 otherwise type 0:\n'))
            
            i += 1
            
            
            self.board = Board()
        
        if not self.human_playing():
            print('at this point the white AI dosen\'t have any possible move that will result in a win but the black AI may not learn all possible cases do you can beat the black AI?' )

    def run(self):

        end = False
        while not end:

            end = self.play(self.WHITE)

            if end == -1:
                return self.BLACK
            if end:
                return self.WHITE

            end = self.play(self.BLACK)
            if end == -1:
                return self.WHITE
        

        self.print(self.board)
        return self.BLACK


    def play(self, turn):
        self.print(self.board)
        if turn:
            self.print('whites')
            played = self.white.play(self.board.pieces.copy())
            if not played:
                return -1

            self.captrue(turn)
        else:
            self.print('blacks')
            played = self.black.play(self.board.pieces.copy())
            if not played:
                return -1
            self.captrue(turn)

        return self.end()
        
    def captrue(self, turn):
        for i in range(len(self.board.pieces)):
            p1 = self.board.pieces[i]
            for j in range(i + 1, len(self.board.pieces)):
                p2 = self.board.pieces[j]
                if p1.pos == p2.pos:
                    if p1.white == turn:
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
        
        if whites == 0 or not white_moves:
            self.print('Blacks wins!')
            return True

        if blacks == 0 or not black_moves:
            self.print('Blacks wins!')
            return True
        
    def human_playing(self) -> bool:
        return type(self.white) is Players.Human or type(self.black) is Players.Human
    
    def print(self, string):
        if self.human_playing():
            print(string)
       