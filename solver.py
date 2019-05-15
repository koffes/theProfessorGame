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
        self.sol_attemp = 0
        self.sol_found = 0

    def _tile_recursive(self, curr_pos):
        # get the next tile to use
        for t in range(16):
            curr_tile = self.deck.get_tile(self.tile_at_pos[curr_pos])
            if curr_tile.get_in_use():
                self.tile_at_pos[curr_pos] = self.tile_at_pos[curr_pos] + 1
                if self.tile_at_pos[curr_pos] >= 16:
                    self.tile_at_pos[curr_pos] = 0
                    return
            else:
                row, col = self.board.tile_push(curr_tile)
                rot = 0
                while rot < 4:
                    # self.disp.board(self.board.board)
                    self.sol_attemp = self.sol_attemp + 1
                    if self.sol_attemp % 50000 == 0:
                        print(self.sol_attemp)
                    if curr_pos >= 14:
                        self.highest_pos = curr_pos
                        # print('curr pos {0} '.format(curr_pos))
                        # print('curr card at pos {0} rot{1}'
                        #      .format(self.tile_at_pos[curr_pos], rot))
                        # print('t {0}'.format(t))

                    if self.board.tile_valid(row, col):
                        if curr_pos == 15:
                            print('Solution found!')
                            self.sol_found = self.sol_found + 1
                            # self.disp.board(self.board.board)
                        else:
                            self._tile_recursive(curr_pos + 1)
                        curr_tile.rotate_cw()
                        rot = rot + 1
                    else:
                        curr_tile.rotate_cw()
                        rot = rot + 1
                self.tile_at_pos[curr_pos] = self.tile_at_pos[curr_pos] + 1
                self.board.tile_pop()
                if self.tile_at_pos[curr_pos] >= 16:
                    self.tile_at_pos[curr_pos] = 0
                    return

        self.tile_at_pos[curr_pos] = 0
        return

    def solve(self):
        """Invoke solver."""
        self.tile_at_pos = [0]*16
        self._tile_recursive(0)
        print('program finished. Soutions found: {}'.format(self.sol_found))
        # self.disp.board(self.board.board)


print('Running the professor game solver.')


s = Solver()
s.solve()
