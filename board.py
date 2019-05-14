"""This file describes the actual four by four board."""
import tiles


class Board:
    """The game board of 4*4 tiles."""

    def __init__(self):
        """Create an empty game board."""
        self.board = [[None for i in range(4)] for j in range(4)]
        print(self.board)

    def _check_next_to_existing_tile(self, row, col):
        if row == 0 and col == 0:
            return
        elif row == 0:
            if self.board[0][col-1] is not None:
                return
        elif col == 0:
            if self.board[row-1][3] is not None:
                return
        else:
            if self.board[row][col-1] is not None:
                return
        raise ValueError('A new tile must be placed next to exisiting tile.')

    def tile_add(self, row, col, tile):
        """Add tile to board."""
        self._check_next_to_existing_tile(row, col)
        if self.board[row][col] is not None:
            raise ValueError('There is already a tile in this spot.')

        if tile.get_in_use():
            raise ValueError('Current tile is already on the board.')
        self.board[row][col] = tile
        self.board[row][col].set_in_use()

    def tile_remove(self, row, col):
        """Remove tile from board."""
        if self.board[row][col] is None:
            raise ValueError('Space is already cleared')
        self.board[row][col].clr_in_use()
        self.board[row][col] = None

    def _edge_match(self, edge_a, edge_b):
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
