"""Professor game solver."""
from deck import Deck
from deck import Display
import tiles


class Solver:
    """Solver for the professor game."""

    def __init__(self):
        """Create the deck and start the solver."""
        self.deck = Deck(tiles.DECK)
        self.disp = Display()
        self.disp.deck(self.deck)


print('Running the professor game solver.')


s = Solver()
