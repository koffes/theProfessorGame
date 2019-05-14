"""Unittests."""
import unittest
from deck import Tile
from deck import Edge
import tiles


class TestTile(unittest.TestCase):
    """Unittests for the Tile class."""

    def setUp(self):
        """Create a Tile with test data."""
        self.edges = [Edge(tiles.Clr.R, tiles.Bprt.T),
                      Edge(tiles.Clr.G, tiles.Bprt.T),
                      Edge(tiles.Clr.B, tiles.Bprt.L),
                      Edge(tiles.Clr.P, tiles.Bprt.L)]
        self.tile = Tile(self.edges)

    def test_in_use(self):
        """Check correct in_use functionality."""
        self.assertFalse(self.tile.get_in_use())
        self.tile.set_in_use()
        self.assertTrue(self.tile.get_in_use())
        self.tile.clr_in_use()
        self.assertFalse(self.tile.get_in_use())

    def test_get_edge(self):
        """Check that all edges are correct."""
        edge = self.tile.get_edge(0)
        self.assertEqual(edge.color.value, 'red')
        self.assertEqual(edge.bdyprt.value, 0)
        edge = self.tile.get_edge(1)
        self.assertEqual(edge.color.value, 'green')
        self.assertEqual(edge.bdyprt.value, 0)
        edge = self.tile.get_edge(2)
        self.assertEqual(edge.color.value, 'blue')
        self.assertEqual(edge.bdyprt.value, 1)
        edge = self.tile.get_edge(3)
        self.assertEqual(edge.color.value, 'purple')
        self.assertEqual(edge.bdyprt.value, 1)

    def test_rotate_cw(self):
        """Check correct rotation."""
        self.tile.set_in_use()
        self.tile.rotate_cw()
        edge = self.tile.get_edge(0)
        self.assertEqual(edge.color.value, 'purple')
        self.assertEqual(edge.bdyprt.value, 1)
        edge = self.tile.get_edge(1)
        self.assertEqual(edge.color.value, 'red')
        self.assertEqual(edge.bdyprt.value, 0)
        edge = self.tile.get_edge(2)
        self.assertEqual(edge.color.value, 'green')
        self.assertEqual(edge.bdyprt.value, 0)
        edge = self.tile.get_edge(3)
        self.assertEqual(edge.color.value, 'blue')
        self.assertEqual(edge.bdyprt.value, 1)


if __name__ == '__main__':
    unittest.main()
