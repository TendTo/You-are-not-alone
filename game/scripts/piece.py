class Piece():

    __slots__ = ["id", "idle", "pos", "align", "zoom", "found"]

    def __init__(self,
                 id,
                 idle=None,
                 pos=None,
                 align=None,
                 zoom=1):  # type: (str, str | None, tuple[float, float] | None, tuple[float, float] | None, float) -> None
        if pos is None and align is None:
            raise ValueError("pos and align cannot be both None")
        self.id = id
        self.idle = idle if idle is not None else id
        self.pos = pos
        self.align = align
        self.zoom = zoom
        self.found = False

    def __eq__(self, x):  # type: (Piece) -> bool
        return isinstance(x, Piece) and self.id == x.id

    def __hash__(self):  # type: () -> int
        return hash(self.id)

    def __ne__(self, x): # type: (Piece) -> bool
        return not self.__eq__(x)
