import renpy.exports as renpy

class Room():

    __slots__ = ["name", "description", "pieces", "nPieces"]

    def __init__(self, name, description, nPieces):
        self.name = name
        self.description = description
        self.nPieces = nPieces
        self.pieces = {i: False for i in range(nPieces) }
    
    def is_complete(self):
        for value in self.pieces.values():
            if not value:
                return None
        return True

    def take_piece(self, idxPiece):
        if idxPiece > self.nPieces:
            raise ValueError("idxPiece must be less than nPieces")
        self.pieces[idxPiece] = True

    def is_piece_taken(self, idxPiece):
        return self.pieces[idxPiece]

    def reset(self):
        self.pieces = {i: False for i in range(self.nPieces) }

    def action_take_piece(self, idxPiece):
        def action():
            self.take_piece(idxPiece)
            if self.is_complete():
                return True
            renpy.restart_interaction()
        return action
