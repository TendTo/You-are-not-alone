import renpy.exports as renpy
from .piece import Piece


class Room():

    __slots__ = ["pieces"]

    def __init__(self, *pieces):  # type: (int, tuple[Piece]) -> None
        self.pieces = list(pieces)  # type: list[Piece]

    def add_pieces(self, pieces):  # type: (list[Piece]) -> None
        self.pieces.extend(pieces)

    def add_piece(self, piece):  # type: (Piece) -> None
        self.pieces.append(piece)

    def is_complete(self):  # type: () -> bool | None
        for piece in self.pieces:
            if not piece.found:
                return None
        return True

    def get_piece(self, idxPiece):  # type: (int | str) -> Piece
        if isinstance(idxPiece, int):
            if idxPiece > len(self.pieces):
                raise ValueError("idxPiece must be less than len(self.pieces)")
            return self.pieces[idxPiece]
        else:
            for piece in self.pieces:
                if piece.id == idxPiece:
                    return piece
            else:
                raise ValueError("idxPiece not found")

    def n_piece_found(self):  # type: () -> int
        n = 0
        for piece in self.pieces:
            if piece.found:
                n += 1
        return n

    def take_piece(self, idxPiece):  # type: (int | str) -> None
        self.get_piece(idxPiece).found = True

    def is_piece_taken(self, idxPiece):  # type: (int | str) -> bool
        return self.get_piece(idxPiece).found

    def reset(self):  # type: () -> None
        self.pieces = []

    def action_take_piece(self, idxPiece):  # type: (int | str) -> None

        def action():
            self.take_piece(idxPiece)
            if self.is_complete():
                return True
            renpy.restart_interaction()

        return action
