"""Professor game solver."""
from deck import Deck
from deck import Display
import tiles


class Board:
    """The actual game board of 4*4 tiles."""

    def __init__(self):
        """Create an empty game board."""
        self.board = [[None for i in range(4)] for j in range(4)]
        print(self.board)

    def tile_add(self, row, col, tile):
        """Add tile to board."""
        if self.board[row][col] is not None:
            raise ValueError('There is already a tile in this spot.')
        self.board[row][col] = tile

    def tile_remove(self, row, col):
        """Remove tile from board."""
        self.board[row][col] = None

    def _edge_match(self, edge_a, edge_b):
        """Check color and bodypart match."""
        if edge_a.color.value is not edge_b.color.value:
            return False
        if edge_a.bdyprt is edge_b.bdyprt:
            return False
        return True

    def tile_valid(self, row, col):
        """Check valid placement in relation to N and W neighbours."""
        if row == 0 and col == 0:
            return True
        elif row == 0:
            return self._edge_match(
                   self.board[0][col-1].get_edge(tiles.DIR_E),
                   self.board[0][col].get_edge(tiles.DIR_W))
        elif col == 0:
            return self._edge_match(
                   self.board[row-1][0].get_edge(tiles.DIR_S),
                   self.board[row][0].get_edge(tiles.DIR_N))
        else:
            return (self._edge_match(
                    self.board[row][col-1].get_edge(tiles.DIR_E),
                    self.board[row][col].get_edge(tiles.DIR_W)) and
                    self._edge_match(
                    self.board[row-1][col].get_edge(tiles.DIR_S),
                    self.board[row][col].get_edge(tiles.DIR_N)))


class Solver:
    """Solver for the professor game."""

    def __init__(self):
        """Create the deck and start the solver."""
        self.deck = Deck(tiles.DECK)
        self.disp = Display()
        self.disp.deck(self.deck)
        self.deck.get_tile(0).rotate_cw()
        self.disp.deck(self.deck)
        self.board = Board()


print('Running the professor game solver.')


s = Solver()
