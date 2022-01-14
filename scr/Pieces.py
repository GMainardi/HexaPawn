class Piece():

    pos = (8,8)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def __init__(self, pos, white) -> None:
        self.pos = pos
        self.white = white

    def moves(self) -> None:
        return []

    def get_name(self) -> None:
        return ''
    
    def valid_pos(self, pos) -> bool:
        return pos[0] > -1 and pos[0] < 8 and pos[1] > -1 and pos[1] < 8

    def empty(self, pos,  pieces) -> tuple:

        for piece in pieces:
            if piece.pos == pos:
                return (piece.white, False)
        
        return (None, True)
    
    def __repr__(self) -> str:
        return str(self.get_name()) + str(chr(self.pos[0]+65))  + str(self.pos[1]+1)
    

class Paw(Piece):

 
    def moves(self, pieces) -> list:

        moves = []

        if self.white:

            attack = self.empty((self.pos[0], self.pos[1]+1), pieces)
            if attack[1]:
                moves.append((self.pos[0], self.pos[1]+1))
            
            attack1 = self.empty((self.pos[0] - 1, self.pos[1]+1), pieces)
            if attack1[0] != None and not attack1[0]:
                moves.append((self.pos[0] - 1, self.pos[1]+1))
            
            attack2 = self.empty((self.pos[0] + 1, self.pos[1]+1), pieces)
            if attack2[0] != None and not attack2[0]:
                moves.append((self.pos[0] + 1, self.pos[1]+1))
        
        if not self.white:
            
            attack = self.empty((self.pos[0], self.pos[1]-1), pieces)
            if attack[1]:
                moves.append((self.pos[0], self.pos[1]-1))
            
            attack1 = self.empty((self.pos[0] - 1, self.pos[1]-1), pieces)
            if attack1[0] != None and attack1[0]:
                moves.append((self.pos[0] - 1, self.pos[1]-1))
            
            attack2 = self.empty((self.pos[0] + 1, self.pos[1]-1), pieces)
            if attack2[0] != None and attack2[0]:
                moves.append((self.pos[0] + 1, self.pos[1]-1))
    
        for move in moves:
            if not self.valid_pos(move):
                moves.remove(move)
    
        return moves
    
    def get_name(self) -> None:
        return 'p'