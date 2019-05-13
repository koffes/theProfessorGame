"""The professor game solver."""
import tiles
import copy
from tkinter import Tk
from tkinter import Canvas
import math
import cmath


class Display:
    """Contains modules for game visualization."""

    def __init__(self):
        """Initialize class for displaying the game board."""
        self.CIRCLE_RADIUS = 10
        self.SIZE_PX = 100
        self.CTR_PX = self.SIZE_PX / 2

    def _circle(self, x, y, r):
        """Draw a circle located at x, y, with radius r."""
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.canvas.create_oval(x0, y0, x1, y1, width=4)

    def _triangle(self, orient, offs_x, offs_y, color, bprt):
        """Draw a triangle (one edge of a tile)."""
        TRI_BASE = [(self.CTR_PX + offs_x, self.CTR_PX + offs_y),
                    (0 + offs_x, 0 + offs_y),
                    (self.SIZE_PX + offs_x, 0 + offs_y),
                    (self.CTR_PX + offs_x, self.CTR_PX + offs_y)]

        rotated_coord = []
        angle = cmath.exp(orient*1j*math.pi/180)
        offs = complex(self.CTR_PX + offs_x, self.CTR_PX + offs_y)
        for x, y in TRI_BASE:
            comp = angle * (complex(x, y) - offs) + offs
            rotated_coord.append(comp.real)
            rotated_coord.append(comp.imag)

        self.canvas.create_polygon(rotated_coord, fill=color.value,
                                   outline='black')

        # If torso, draw a circle to indicate on top of triangle
        if bprt == tiles.Bprt.T:
            comp = angle * (complex(offs_x + self.CTR_PX, offs_y + 15) -
                            offs) + offs
            self._circle(comp.real, comp.imag, self.CIRCLE_RADIUS)

        # If legs, draw a line
        if bprt == tiles.Bprt.L:
            comp_s = angle * (complex(offs_x + self.CTR_PX, offs_y + 5) -
                              offs) + offs
            comp_e = angle * (complex(offs_x + self.CTR_PX, offs_y + 25) -
                              offs) + offs
            self.canvas.create_line(comp_s.real, comp_s.imag,
                                    comp_e.real, comp_e.imag, width=4)

        self.canvas.create_rectangle(offs_x, offs_y,
                                     offs_x + self.SIZE_PX,
                                     offs_y + self.SIZE_PX, width=4)

    def deck(self, deck):
        """Draw the entire tile deck."""
        root = Tk()
        self.canvas = Canvas(width=self.SIZE_PX * tiles.EDGE_NUM,
                             height=self.SIZE_PX * tiles.EDGE_NUM, bg='white')
        self.canvas.pack()

        for i, tile in enumerate(deck.tiles, start=0):
            x, y = divmod(i, tiles.EDGE_NUM)
            for j, edge in enumerate(tile.get_edges(), start=0):
                self._triangle(j * 90, x * 100, y * 100,
                               edge.color, edge.bdyprt)

        root.mainloop()


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
        if not self.in_use:
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
        if len(init_deck) != tiles.CARDS_NUM:
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
