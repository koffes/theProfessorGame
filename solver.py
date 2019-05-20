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
        self.tile_idx_last = 0

    def _prog_monit(self, curr_pos, tile_idx):
        self.sol_attemp += 1
        if self.sol_attemp % 100000 == 0:
            print('Solutions tried: {0}'.format(self.sol_attemp))
        if curr_pos == 0 and tile_idx > self.tile_idx_last:
            self.tile_idx_last = tile_idx
            print('Prog {0:.2f} %'.format(tile_idx * 100 / tiles.TILES_NUM))

    def _tile_rotation(self, curr_pos, row, col, curr_tile):
        rot = 0
        while rot < tiles.EDGE_NUM:
            if self.board.tile_valid(row, col):
                if curr_pos == (tiles.TILES_NUM - 1):
                    self.sol_found += 1
                    print('Solution! num: {0}'.format(self.sol_found))
                    save_filename = 'solutions/sol_'+str(self.sol_found)+'.eps'
                    self.disp.board(self.board.board, False, save_filename)
                else:
                    self._tile_recursive(curr_pos + 1)
                curr_tile.rotate_cw()
                rot += 1
            else:
                curr_tile.rotate_cw()
                rot += 1

    def _tile_recursive(self, curr_pos):
        """Curr pos indicates current board tile."""
        for tile_idx in range(tiles.TILES_NUM):
            curr_tile = self.deck.get_tile(self.tile_at_pos[curr_pos])
            if curr_tile.get_in_use():
                self.tile_at_pos[curr_pos] += 1
                if self.tile_at_pos[curr_pos] >= tiles.TILES_NUM:
                    self.tile_at_pos[curr_pos] = 0
                    return
            else:
                row, col = self.board.tile_push(curr_tile)
                self._prog_monit(curr_pos, tile_idx)
                self._tile_rotation(curr_pos, row, col, curr_tile)
                self.tile_at_pos[curr_pos] += 1
                self.board.tile_pop()
                if self.tile_at_pos[curr_pos] >= tiles.TILES_NUM:
                    self.tile_at_pos[curr_pos] = 0
                    return

        self.tile_at_pos[curr_pos] = 0
        return

    def solve(self):
        """Invoke solver."""
        self.tile_at_pos = [0]*tiles.TILES_NUM
        self._tile_recursive(0)
        print('program finished. Solutions found: {}'.format(self.sol_found))
        return self.sol_found


print('Running the professor game solver.')


s = Solver()
s.solve()
