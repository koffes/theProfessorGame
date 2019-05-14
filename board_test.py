"""Unittests."""
import unittest
from deck import Tile
from board import Board
from deck import Edge
import tiles


class TestBoard(unittest.TestCase):
    """Unittests for the Tile class."""

    def setUp(self):
        """Create a Tile with test data."""
        self.board = Board()
        self.edges_1 = [Edge(tiles.Clr.R, tiles.Bprt.T),
                        Edge(tiles.Clr.G, tiles.Bprt.T),
                        Edge(tiles.Clr.B, tiles.Bprt.L),
                        Edge(tiles.Clr.P, tiles.Bprt.L)]
        self.edges_2 = [Edge(tiles.Clr.R, tiles.Bprt.T),
                        Edge(tiles.Clr.G, tiles.Bprt.T),
                        Edge(tiles.Clr.B, tiles.Bprt.L),
                        Edge(tiles.Clr.G, tiles.Bprt.L)]
        self.edges_3 = [Edge(tiles.Clr.B, tiles.Bprt.T),
                        Edge(tiles.Clr.G, tiles.Bprt.T),
                        Edge(tiles.Clr.B, tiles.Bprt.L),
                        Edge(tiles.Clr.G, tiles.Bprt.L)]
        self.edges_4 = [Edge(tiles.Clr.B, tiles.Bprt.T),
                        Edge(tiles.Clr.G, tiles.Bprt.T),
                        Edge(tiles.Clr.B, tiles.Bprt.L),
                        Edge(tiles.Clr.G, tiles.Bprt.L)]

        self.tile_a = Tile(self.edges_1)
        self.tile_b = Tile(self.edges_2)
        self.tile_c = Tile(self.edges_2)
        self.tile_d = Tile(self.edges_2)
        self.tile_e = Tile(self.edges_3)
        self.tile_f = Tile(self.edges_4)
        self.tile_g = Tile(self.edges_1)

    def test_tile_add(self):
        """Check that multiple tiles can be added to board."""
        self.board.tile_add(0, 0, self.tile_a)
        self.board.tile_add(0, 1, self.tile_b)

    def test_tile_add_twice(self):
        """Shall raise exception if same tile is present twice."""
        self.board.tile_add(0, 0, self.tile_a)
        self.assertRaises(ValueError, self.board.tile_add, 0, 1, self.tile_a)

    def test_same_position_used(self):
        """Shall raise exception if board position is already taken."""
        self.board.tile_add(0, 0, self.tile_a)
        self.assertRaises(IndexError, self.board.tile_add, 0, 0, self.tile_b)

    def test_adjacent_position(self):
        """Correct positioning of new tile."""
        self.board.tile_add(0, 0, self.tile_a)
        self.board.tile_add(0, 1, self.tile_b)
        self.board.tile_add(0, 2, self.tile_c)
        self.board.tile_add(0, 3, self.tile_d)
        self.board.tile_add(1, 0, self.tile_e)

    def test_not_adjacent_position_a(self):
        """Raise exception if tile is not placed adjacent to existing tile."""
        self.board.tile_add(0, 0, self.tile_a)
        self.assertRaises(IndexError, self.board.tile_add, 0, 2, self.tile_b)

    def test_not_adjacent_position_b(self):
        """Raise exception if tile is not placed adjacent to existing tile."""
        self.board.tile_add(0, 0, self.tile_a)
        self.assertRaises(IndexError, self.board.tile_add, 1, 0, self.tile_b)

    def test_tile_push_pop(self):
        """Push and pop from list. Finally pop beyond upper limit."""
        self.board.tile_push(self.tile_a)
        self.board.tile_push(self.tile_b)
        self.board.tile_pop()
        self.board.tile_pop()
        self.assertRaises(IndexError, self.board.tile_pop)

    def test_valid(self):
        """Test that the valid placement checks are working."""
        # First tile shall always be valid
        row, col = self.board.tile_push(self.tile_a)
        self.assertTrue(self.board.tile_valid(row, col))
        # Place valid tile
        row, col = self.board.tile_push(self.tile_b)
        self.assertTrue(self.board.tile_valid(row, col))
        # Place valid tile
        row, col = self.board.tile_push(self.tile_c)
        self.assertTrue(self.board.tile_valid(row, col))
        # Place valid tile
        row, col = self.board.tile_push(self.tile_d)
        self.assertTrue(self.board.tile_valid(row, col))
        # Place valid tile
        row, col = self.board.tile_push(self.tile_e)
        self.assertTrue(self.board.tile_valid(row, col))
        # Place valid tile
        row, col = self.board.tile_push(self.tile_f)
        self.assertTrue(self.board.tile_valid(row, col))
        # Remove valid tile
        self.board.tile_pop()
        # Place invalid tile
        row, col = self.board.tile_push(self.tile_g)
        self.assertFalse(self.board.tile_valid(row, col))


if __name__ == '__main__':
    unittest.main()
