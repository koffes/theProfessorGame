import cards
import copy
from tkinter import Tk
from tkinter import Canvas
import math
import cmath


TRI_E = [50, 50, 100, 0, 100, 100, 50, 50]
TRI_S = [50, 50, 100, 100, 0, 100, 50, 50]
TRI_W = [50, 50, 0, 100, 0, 0, 50, 50]


class Draw:
    def __init__(self):
        self.CIRCLE_RADIUS = 10
        self.COORD_CENTER = 50
        self.N = 0
        self.E = 90
        self.S = 180
        self.W = 270

    def _circle(self, x, y, r):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.canvas.create_oval(x0, y0, x1, y1, width=4)

    def _triangle(self, orient, offs_x, offs_y, color, bprt):
        TRI_BASE = [(50 + offs_x, 50 + offs_y),
                    (0 + offs_x, 0 + offs_y),
                    (100 + offs_x, 0 + offs_y),
                    (50 + offs_x, 50 + offs_y)]

        rotated_coord = []
        angle = cmath.exp(orient*1j*math.pi/180)
        offs = complex(self.COORD_CENTER + offs_x, self.COORD_CENTER + offs_y)
        for x, y in TRI_BASE:
            print(x)
            print(y)
            comp = angle * (complex(x, y) - offs) + offs
            rotated_coord.append(comp.real)
            rotated_coord.append(comp.imag)

        self.canvas.create_polygon(rotated_coord, fill=color)

        # If we have a torso, draw a circle to indicate on top of triangle
        if bprt == cards.Bprt.T:
            comp = angle * (complex(50, 20) - offs) + offs
            self._circle(comp.real, comp.imag, self.CIRCLE_RADIUS)

    def deck(self, deck):
        root = Tk()
        self.canvas = Canvas(width=400, height=400, bg='white')
        self.canvas.pack()
        self._triangle(self.S, 0, 0, 'red', cards.Bprt.T)
        root.mainloop()

        i = 0
        for card in deck.cards:
            for side in card.sides:
                # print('side {}'.format(i))
                i = i + 1


class Side:
    def __init__(self, color, bdyprt):
        self.color = color
        self.bdyprt = bdyprt


class Card:
    def __init__(self, sides):
        if len(sides) != cards.SIDE_NUM:
            raise ValueError('The number of card sides is incorrect')

        self.sides = copy.deepcopy(sides)
        for side in self.sides:
            print('{}'.format(side.color))

    def get_side(self, i):
        return self.sides[i]


class Deck:
    def __init__(self, init_deck):
        if len(init_deck) != cards.CARDS_NUM:
            raise ValueError('The number of card in deck is incorrect')

        self.cards = []
        for card in range(len(init_deck)):
            print(card)
            sides = []
            for side in range(len(init_deck[0])):
                sides.append(Side(init_deck[card][side][0],
                                  init_deck[card][side][1]))
            self.cards.append(Card(sides))

    def get_card(self, i):
        return self.cards[i]


print('running prog')
deck = Deck(cards.DECK)
draw = Draw()
draw.deck(deck)
