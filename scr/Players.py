import Pieces
from random import randint, shuffle

class Player():


    def __init__(self, white) -> None:
        self.white = white
        pass

    def play(self, pieces) -> None:
        pass
    

    def find_piece(self, pieces, pos) -> Pieces.Piece:
        pass


class Human(Player):

    def play(self, pieces) -> None:
        my_pieces = [p for p in pieces if p.white == self.white]
        while True:
            pos = int(input('what piece do you want to move?\n')) -1
            piece = self.find_piece(my_pieces,pos)
            if not piece:
                continue
            break

        
        do = True
        while do:
            pos = int(input('what is your move?\n')) -1
            pos = (pos//3, pos%3)
            for move in piece.moves(pieces):
                if move == pos:
                    piece.pos = move
                    do = False
                    break
        return True

    def find_piece(self, pieces, pos) -> Pieces.Piece:
        pos = (pos//3, pos%3)
        for piece in pieces:
                if piece.pos == pos:
                    return piece
        print('Piece not found')

class AI(Player):
    
    states = {}
    last_move = None

    def play(self, pieces) -> None:
        state = tuple([str(piece) for piece in pieces])

        if not state in self.states.keys():
            my_pieces = [p for p in pieces if p.white == self.white]
            moves = [(str(piece), move) for piece in my_pieces for move in piece.moves(pieces)]
            self.states[state] = moves
        

        moves = self.states[state]
        if not len(moves):
            return False
        random_move = randint(0, len(moves)-1)
        piece, move = moves[random_move]
        piece = self.find_piece(pieces, piece)
        piece.pos = move
        self.last_move = (state, random_move)
        return True

    
    def learn(self):
        if self.last_move:
            state, move_id = self.last_move
            del self.states[state][move_id]
            self.last_move = None
            return True
        else:
            return False
        

    def find_piece(self, pieces, p) -> Pieces.Piece:
        for piece in pieces:
            if str(piece) == p:
                return piece
        print('Piece not found')


class MonteCarlo(Player):
    

    def play(self, pieces) -> None:

        from  Board import Board
        from Game import Game

        my_pieces = [p for p in pieces if p.white == self.white]
        moves = [(str(piece), move) for piece in my_pieces for move in piece.moves(pieces)]

        best_move = None
        best_wins = 0
        
        # for each possible move
        for piece, move in moves:

            wins = 0
            # simulate 10 games with that move
            for _ in range(10):
                hipo_board = Board(pieces)
                hipo_game = Game(-1, -1, hipo_board, self.white)

                # makes hipotetic move
                hipo_piece = self.find_piece(hipo_board.pieces, piece)
                hipo_piece.pos = move
                hipo_game.captrue()
                end = hipo_game.end()
                if end:
                    wins += 1
                    continue
                hipo_game.turn = not self.white
                # simulate the game
                winner = hipo_game.run()
                if winner == self.white:
                    wins += 1
            # get the move who wins more random games
            if wins >= best_wins:
                best_wins = wins
                best_move = (piece, move)
        # make the choosed move
        piece, move = best_move
        piece = self.find_piece(my_pieces, piece)
        piece.pos = move
        return True


    def find_piece(self, pieces, p) -> Pieces.Piece:
        for piece in pieces:
            if str(piece) == str(p):
                return piece
        print('Piece not found')
    

class Random(Player):

    def play(self, pieces) -> None:
        my_pieces = [p for p in pieces if p.white == self.white]

        smart = self.smart_move(pieces)
        if smart:
            return True

        shuffle(my_pieces)
        for piece in my_pieces:
            moves = piece.moves(pieces)
            if len(moves):
                move_id = randint(0, len(moves)-1)
                move = moves[move_id]
                piece.pos = move
                return True 
            else:
                continue
        return -1

    def smart_move(self, pieces):
        from Board import Board
        my_pieces = [p for p in pieces if p.white == self.white]
        enimy_pieces = [p for p in pieces if p.white != self.white]

        for piece in my_pieces:
            for move in piece.moves(pieces):

                if len(enimy_pieces) == 1 and move == enimy_pieces[0].pos:
                    piece.pos = move
                    return True
                if self.white:
                    if move[1] == 2:
                        piece.pos = move
                        return True
                else:
                    if move[1] == 0:
                        piece.pos = move
                        return True

                hip_board = Board(pieces)
                hip_piece = self.find_piece(hip_board.pieces, piece)
                hip_piece.pos = move
                enimy_moves = 0
                for enimy in hip_board.pieces:
                    if enimy.white != self.white:
                        enimy_moves += len(enimy.moves(hip_board.pieces))
                if enimy_moves == 0:
                    piece.pos = move
                    return True

        return False
    
    def find_piece(self, pieces, p) -> Pieces.Piece:
        for piece in pieces:
            if str(piece) == str(p):
                return piece
        print('Piece not found')