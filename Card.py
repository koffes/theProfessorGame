"""The professor game solver."""
import cards
import copy
from tkinter import Tk
from tkinter import Canvas
import math
import cmath


class Draw:
    """Contains modules for game visualization."""

    def __init__(self):
        """Initialize class for drawing the game board."""
        self.CIRCLE_RADIUS = 10
        self.COORD_CENTER = 50
        self.CARDINAL_N = 0
        self.CARDINAL_E = 90
        self.CARDINAL_S = 180
        self.CARDINAL_W = 270

    def _circle(self, x, y, r):
        """Draw a circle located at x, y, with radius r."""
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.canvas.create_oval(x0, y0, x1, y1, width=4)

    def _triangle(self, orient, offs_x, offs_y, color, bprt):
        """Draw a triangle (one edge of a card)."""
        TRI_BASE = [(50 + offs_x, 50 + offs_y),
                    (0 + offs_x, 0 + offs_y),
                    (100 + offs_x, 0 + offs_y),
                    (50 + offs_x, 50 + offs_y)]

        rotated_coord = []
        angle = cmath.exp(orient*1j*math.pi/180)
        offs = complex(self.COORD_CENTER + offs_x, self.COORD_CENTER + offs_y)
        for x, y in TRI_BASE:
            comp = angle * (complex(x, y) - offs) + offs
            rotated_coord.append(comp.real)
            rotated_coord.append(comp.imag)

        self.canvas.create_polygon(rotated_coord, fill=color.value,
                                   outline='black')

        # If we have a torso, draw a circle to indicate on top of triangle
        if bprt == cards.Bprt.T:
            comp = angle * (complex(offs_x + 50, offs_y + 15) - offs) + offs
            self._circle(comp.real, comp.imag, self.CIRCLE_RADIUS)

        if bprt == cards.Bprt.L:
            comp_s = angle * (complex(offs_x + 50, offs_y + 5) - offs) + offs
            comp_e = angle * (complex(offs_x + 50, offs_y + 25) - offs) + offs
            self.canvas.create_line(comp_s.real, comp_s.imag,
                                    comp_e.real, comp_e.imag, width=4)

        self.canvas.create_rectangle(offs_x, offs_y,
                                     offs_x + 100, offs_y + 100, width=4)

    def deck(self, deck):
        """Draw the entire card deck."""
        root = Tk()
        self.canvas = Canvas(width=400, height=400, bg='white')
        self.canvas.pack()

        for i, card in enumerate(deck.cards, start=0):
            x, y = divmod(i, cards.EDGE_NUM)
            for j, edge in enumerate(card.edges, start=0):
                self._triangle(j * 90, x * 100, y * 100,
                               edge.color, edge.bdyprt)

        root.mainloop()


class Side:
    """Class describing one edge of a card."""

    def __init__(self, color, bdyprt):
        """Initialize a edge of a card. A card has four edges."""
        self.color = color
        self.bdyprt = bdyprt


class Card:
    """Class description of a single card."""

    def __init__(self, edges):
        """Create a card with four edges."""
        if len(edges) != cards.EDGE_NUM:
            raise ValueError('The number of card edges is incorrect')

        self.edges = copy.deepcopy(edges)
        # for edge in self.edges:
        # print('{}'.format(edge.color))

    def get_edge(self, i):
        """Get a card edge. Labelled clockwise from North."""
        return self.edges[i]


class Deck:
    """Contains the entire 16 card player deck."""

    def __init__(self, init_deck):
        """Create a deck of cards."""
        if len(init_deck) != cards.CARDS_NUM:
            raise ValueError('The number of card in deck is incorrect')

        self.cards = []
        for card in range(len(init_deck)):
            edges = []
            for edge in range(len(init_deck[0])):
                edges.append(Side(init_deck[card][edge][0],
                                  init_deck[card][edge][1]))
            self.cards.append(Card(edges))

    def get_card(self, i):
        """Get a card."""
        return self.cards[i]


print('Running the professor game solver.')
deck = Deck(cards.DECK)
draw = Draw()
draw.deck(deck)
