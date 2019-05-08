from enum import Enum

CARDS_NUM = 16
SIDE_NUM = 4
BPRT_NUM = 2


class Bprt(Enum):
    T = 0
    L = 1


class Clr(Enum):
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

print(DECK)
