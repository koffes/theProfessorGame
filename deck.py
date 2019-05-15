"""The professor game solver."""
import tiles
import copy


class Edge:
    """Class describing one edge of a tile."""

    def __init__(self, color, bdyprt):
        """Initialize a edge of a tile. A tile has four edges."""
        self.color = color
        self.bdyprt = bdyprt


class Tile:
    """Class description of a single tile."""

    def __init__(self, edges):
        """Create a tile with four edges."""
        if len(edges) != tiles.EDGE_NUM:
            raise ValueError('The number of tile edges is incorrect')

        self._edges = copy.deepcopy(edges)
        self._original_edges = self._edges
        self._in_use = False

    def get_edge(self, i):
        """Get a tile edge. Labelled clockwise from North."""
        return self._edges[i]

    def get_edges(self):
        """Return all edges."""
        return self._edges

    def rotate_cw(self):
        """Rotate card clockwise."""
        if not self._in_use:
            raise RuntimeError('Tile not in use shall not be rotated')
        self._edges = [self._edges[-1]] + self._edges[0:-1]

    def set_in_use(self):
        """Tile is used in board."""
        self._in_use = True

    def clr_in_use(self):
        """Return to original rotation."""
        self._edges = self._original_edges
        self._in_use = False

    def get_in_use(self):
        """Check if given tile is placed."""
        return self._in_use


class Deck:
    """Contains the entire 16 tile player deck."""

    def __init__(self, init_deck):
        """Create a deck of tiles."""
        if len(init_deck) != tiles.TILES_NUM:
            raise ValueError('The number of tile in deck is incorrect')

        self.tiles = []
        for tile in range(len(init_deck)):
            edges = []
            for edge in range(len(init_deck[0])):
                edges.append(Edge(init_deck[tile][edge][0],
                                  init_deck[tile][edge][1]))
            self.tiles.append(Tile(edges))

    def get_tile(self, i):
        """Get a tile."""
        return self.tiles[i]
