import Pieces
from termcolor import colored

class Board():

    

    def __init__(self) -> None:
        self.pieces = []
        # adding Pawns to the board
        for i in range(3):
            pass
            self.pieces.append(Pieces.Paw((i, 0), True))
            self.pieces.append(Pieces.Paw((i, 2), False))


    def moves(self, piece):
        return piece.moves(self.pieces)

    def get_pece_in_place(self, place):
        for p in self.pieces:
            if p.pos == place:
                return colored(p.get_name().upper(), 'white') if p.white else colored(p.get_name().upper(), 'grey')
        return ' '


    def __repr__(self) -> str:
        out = ''
        for x in range(3):
            out += '+---'*3 + '+' + '\n'
            for y in range(3):
                out += f'| {self.get_pece_in_place((x,y))} '
            out += '|' + '\n'
        out += '+---'*3 + '+' + '\n'
        return out
    
    def help(self) -> None:

        print()
        print('Welcome to the HexaPawn game, that game have 6 pieces with the moves similars to pawn in chess game')
        print('Each player has 3 pawns and the goal is reach the other side of the board, or capture all enimy pawns')
        print("The board is mapped with numbers from 1 to 9 as your numpad keys: ")
        
        for x in range(3):
            print('+---'*3 + '+')
            for y in range(3):
                print(f'| {x+(3*y)} ', end='')
            print('|')
        print('+---'*3 + '+')
        print()