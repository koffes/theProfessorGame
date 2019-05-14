"""Professor game solver."""
from deck import Deck
import tiles
from display import Display
from board import Board


class Solver:
    """Solver for the professor game."""

    def __init__(self):
        """Create the deck and start the solver."""
        self.deck = Deck(tiles.DECK)
        self.disp = Display()
        self.board = Board()
        self.board.tile_add(0, 0, self.deck.get_tile(0))
        self.disp.board(self.board.board)


print('Running the professor game solver.')


s = Solver()
