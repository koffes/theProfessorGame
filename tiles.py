"""Description of the cards and the given deck."""
from enum import Enum

TILES_NUM = 16
EDGE_NUM = 4
DIR_N = 0
DIR_E = 1
DIR_S = 2
DIR_W = 3


class Bprt(Enum):
    """The two possible side bodyparts. Torso or legs."""

    T = 0
    L = 1


class Clr(Enum):
    """All possible edge colors."""

    G = 'green'
    R = 'red'
    P = 'purple'
    B = 'blue'


DECK = [
    [[Clr.P, Bprt.L], [Clr.G, Bprt.T], [Clr.B, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.G, Bprt.L], [Clr.R, Bprt.T], [Clr.P, Bprt.T], [Clr.B, Bprt.L]],
    [[Clr.B, Bprt.L], [Clr.R, Bprt.T], [Clr.P, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.P, Bprt.L], [Clr.B, Bprt.T], [Clr.R, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.B, Bprt.L], [Clr.P, Bprt.T], [Clr.G, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.P, Bprt.L], [Clr.R, Bprt.T], [Clr.B, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.B, Bprt.L], [Clr.G, Bprt.T], [Clr.G, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.P, Bprt.L], [Clr.G, Bprt.T], [Clr.B, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.P, Bprt.L], [Clr.R, Bprt.T], [Clr.B, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.G, Bprt.L], [Clr.B, Bprt.T], [Clr.P, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.G, Bprt.L], [Clr.G, Bprt.T], [Clr.P, Bprt.T], [Clr.R, Bprt.L]],
    [[Clr.R, Bprt.L], [Clr.R, Bprt.T], [Clr.B, Bprt.T], [Clr.B, Bprt.L]],
    [[Clr.B, Bprt.L], [Clr.G, Bprt.T], [Clr.P, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.R, Bprt.L], [Clr.P, Bprt.T], [Clr.B, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.G, Bprt.L], [Clr.R, Bprt.T], [Clr.P, Bprt.T], [Clr.G, Bprt.L]],
    [[Clr.P, Bprt.L], [Clr.G, Bprt.T], [Clr.R, Bprt.T], [Clr.R, Bprt.L]]]
