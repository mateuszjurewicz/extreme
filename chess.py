class Game:
    pass


class Piece:
    pass


class Board(object):
    """
    A chess board object.
    """

    def __init__(self, num_columns, num_rows):
        self.num_columns = num_columns
        self.num_rows = num_rows

    def __repr__(self):
        return "repr"

    def __str__(self):
        return str(self.num_columns)


if __name__ == "__main__":

    our_board = Board(10, 10)
    print(our_board)