''' Structural Game for 15 - Puzzle with different difficulty levels'''
import renpy.exports as renpy
import renpy.display as display
from random import choice


class FifteenSquare:

    __slots__ = ["id", "idle", "w", "h", "x", "y", "origin_x", "origin_y"
                 "pos"]

    def __init__(self, id, idle, square_size, origin_pos, grid_pos):
        # type: (str, str, tuple[int, int], tuple[int, int], tuple[int, int]) -> None
        self.id = id
        self.idle = idle
        self.w, self.h = square_size
        self.origin_x, self.origin_y = origin_pos
        self.x, self.y = grid_pos
        self.pos = (self.origin_x + self.x * self.w, self.origin_y + self.y * self.h)

    def update_grid_pos(self, grid_pos):
        # type: (tuple[int, int]) -> None
        self.x, self.y = grid_pos
        self.update_pos()

    def update_pos(self):
        # type: () -> None
        self.pos = (self.origin_x + self.x * self.w, self.origin_y + self.y * self.h)

    def __eq__(self, x):
        # type: (FifteenSquare) -> bool
        return isinstance(x, FifteenSquare) and self.id == x.id

    def __hash__(self):
        # type: () -> int
        return hash(self.id)

    def __ne__(self, x):
        # type: (FifteenSquare) -> bool
        return not self.__eq__(x)


class Fifteen():

    __slots__ = [
        "origin_pos", "square_size", "x", "y", "initial_square_position", "squares"
        "empty_position", "last_fro", "last_to"
    ]

    @classmethod
    def from_file(cls, filename, origin_pos, square_size, size):
        # type: (str, tuple[int, int], tuple[int, int], tuple[int, int], bool | None) -> Fifteen
        squares = []
        for y in range(size[1]):
            for x in range(size[0]):
                if x == size[0] - 1 and y == size[1] - 1:
                    break
                picture = "%s-%s-%s" % (filename, str(x + 1).zfill(2), str(y + 1).zfill(2))
                square = FifteenSquare(id=picture,
                                       idle=picture,
                                       square_size=square_size,
                                       grid_pos=(x, y),
                                       origin_pos=origin_pos)
                squares.append(square)
        return cls(squares, origin_pos, square_size, size)

    def __init__(self, squares, origin_pos, square_size, size):
        # type: (list[FifteenSquare], tuple[int, int], tuple[int, int], tuple[int, int]) -> None
        (self.w, self.h) = size
        if len(squares) != self.w * self.h - 1:
            raise ValueError("the number of squares must be size[0] * size[1] - 1")
        self.origin_pos = origin_pos
        self.square_size = square_size
        self.initial_square_position = squares
        self.squares = [squares[i] if i < len(squares) else None for i in range(self.w * self.h)]
        self.empty_position = len(self.squares) - 1
        self.last_fro = 0
        self.last_to = 0

    def adj_pos(self, pos):
        # type: (int | tuple[int, int]) -> tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int]
        if isinstance(pos, int):
            return (pos - 1, pos + 1, pos - 4, pos + 4)
        return (pos[0] - 1, pos[0] + 1, pos[1] - 1, pos[1] + 1)

    def get_valid_fro(self):  # type: () -> tuple[int]
        (x, y) = self.get_mat_pos(self.empty_position)
        valid_moves = []
        if x != 0:
            valid_moves.append(self.get_arr_pos((x - 1, y)))
        if x != self.w - 1:
            valid_moves.append(self.get_arr_pos((x + 1, y)))
        if y != 0:
            valid_moves.append(self.get_arr_pos((x, y - 1)))
        if y != self.h - 1:
            valid_moves.append(self.get_arr_pos((x, y + 1)))
        return tuple(valid_moves)

    def get_mat_pos(self, pos):  # type: (int | tuple[int, int] | FifteenSquare) -> tuple[int, int]
        if isinstance(pos, int):
            return (pos % self.w, pos // self.w)
        if isinstance(pos, FifteenSquare):
            for (i, square) in enumerate(self.squares):
                if square == pos:
                    return (i % self.w, i // self.w)
            raise ValueError("piece not found")
        return pos

    def get_arr_pos(self, pos):  # type: (int | tuple[int, int] | FifteenSquare) -> int
        if isinstance(pos, int):
            return pos
        if isinstance(pos, FifteenSquare):
            for (i, square) in enumerate(self.squares):
                if square == pos:
                    return i
            raise ValueError("piece not found")
        return pos[1] * self.w + pos[0]

    def get_square(self, pos):  # type: (int | tuple[int, int]) -> FifteenSquare
        if isinstance(pos, int):
            return self.squares[pos]
        return self.squares[pos[1] * self.w + pos[0]]

    def move(self, fro):  # type: (int | tuple[int, int]) -> None
        self.swap_squares(fro, self.empty_position)
        self.empty_position = self.get_arr_pos(fro)

    def swap_squares(self, fro, to):  # type: (int | tuple[int, int], int | tuple[int, int]) -> None
        from_square = self.get_square(fro)
        to_square = self.get_square(to)

        if from_square is not None:
            from_square.update_grid_pos(self.get_mat_pos(to))
        if to_square is not None:
            to_square.update_grid_pos(self.get_mat_pos(fro))

        arr_fro = self.get_arr_pos(fro)
        arr_to = self.get_arr_pos(to)
        self.squares[arr_fro] = to_square
        self.squares[arr_to] = from_square

        self.last_fro = arr_fro
        self.last_to = arr_to

    def shuffle(self, moves=50):  # type: (int) -> None
        for _ in range(moves):
            fros = [fro for fro in self.get_valid_fro() if fro != self.last_to]
            self.move(choice(fros))

        if self.is_solved():
            self.shuffle(moves)
        self.last_fro = -1
        self.last_to = -1

    def is_solved(self):  # type: () -> bool
        for (i, square) in enumerate(self.initial_square_position):
            if self.squares[i] != square:
                return False
        return True

    def get_action_classic(self, square):  # type: (FifteenSquare) -> None

        def action():
            valid_squares = [self.get_square(fro) for fro in self.get_valid_fro()]
            if square in valid_squares:
                self.move((square.x, square.y))
            else:
                self.highlight(valid_squares)
            if self.is_solved():
                return True
            renpy.restart_interaction()

        return action

    def get_action_teleport(self, square):  # type: (FifteenSquare) -> None

        def action():
            square_pos = self.get_arr_pos((square.x, square.y))
            self.move(square_pos)
            if self.is_solved():
                return True
            renpy.restart_interaction()

        return action

    def get_action_no_error(self, square):  # type: (FifteenSquare) -> None

        def action():
            valid_squares = [self.get_square(fro) for fro in self.get_valid_fro() if fro != self.last_to]
            if square in valid_squares:
                self.move((square.x, square.y))
            else:
                self.highlight(valid_squares)
            if self.is_solved():
                return True
            renpy.restart_interaction()

        return action

    def highlight(self, valid_squares):
        # type: (list[FifteenSquare]) -> None
        for (i, valid_square) in enumerate(valid_squares):
            t = display.transform.Transform(pos=valid_square.pos, anchor=(0, 0), xysize=self.square_size)
            renpy.show("highlight%d" % i, at_list=[t], layer="highlight")
