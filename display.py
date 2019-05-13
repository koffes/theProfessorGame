"""Display functions for the game deck and board."""
from tkinter import Tk
from tkinter import Canvas
import tiles
import math
import cmath


class Display:
    """Contains modules for game visualization."""

    def __init__(self):
        """Initialize class for displaying the game board."""
        self.CIRCLE_RADIUS = 10
        self.SIZE_PX = 100
        self.CTR_PX = self.SIZE_PX / 2
        self.tk_root = Tk()
        self.canvas = Canvas(width=self.SIZE_PX * tiles.EDGE_NUM,
                             height=self.SIZE_PX * tiles.EDGE_NUM, bg='white')
        self.canvas.pack()

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

        if color is None:
            self.canvas.create_polygon(rotated_coord, fill='gray',
                                       outline='black')
        else:
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
        for i, tile in enumerate(deck.tiles, start=0):
            row, col = divmod(i, tiles.EDGE_NUM)
            for edge_no, edge in enumerate(tile.get_edges(), start=0):
                self._triangle(edge_no * 90, col * 100, row * 100,
                               edge.color, edge.bdyprt)

        self.tk_root.mainloop()

    def board(self, board):
        """Draw the board."""
        for row in range(tiles.EDGE_NUM):
            for col in range(tiles.EDGE_NUM):
                if board[row][col] is None:
                    for edge_no in range(tiles.EDGE_NUM):
                        self._triangle(edge_no * 90, col * 100, row * 100,
                                       None, None)
                else:
                    for edge_no, edge in enumerate(board[row][col].get_edges(),
                                                   start=0):
                        self._triangle(edge_no * 90, col * 100, row * 100,
                                       edge.color, edge.bdyprt)
        self.tk_root.mainloop()
