class Piece():
    def __init__(self, id, idle, pos, zoom = 1): # type: (str, str, tuple[float, float], float) -> None
        self.id = id
        self.idle = idle
        self.pos = pos
        self.zoom = zoom
        self.found = False