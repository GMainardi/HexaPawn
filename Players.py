import Pieces
from random import randint

class Player():


    def __init__(self, white) -> None:
        self.white = white
        pass

    def play(self, pieces) -> None:
        pass
    

    def find_piece(self, pieces, pos) -> Pieces.Piece:
        pos = (pos//3, pos%3)
        for piece in pieces:
                if piece.pos == pos:
                    return piece
        print('Piece not found')


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


