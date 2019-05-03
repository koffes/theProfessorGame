import cards
import copy


class Side:
    def __init__(self, color, bdyprt):
        self.color = color
        self.bdyprt = bdyprt


class Card:
    def __init__(self, sides):
        if len(sides) != cards.SIDE_NUM:
            raise ValueError('The number of card sides is incorrect')

        self.card = copy.deepcopy(sides)
        for side in self.card:
            print('{}'.format(side.color))


print('running prog')
s0 = Side(1, 2)
s1 = Side(3, 4)
s2 = Side(5, 6)
s3 = Side(7, 8)

sides = []
sides.append(s0)
sides.append(s1)
sides.append(s2)
sides.append(s3)


kort = Card(sides)
