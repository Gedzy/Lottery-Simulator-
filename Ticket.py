#!/usr/bin/python
# -*- coding: utf-8 -*-

try:

    from Ball import Ball

except KeyboardInterrupt:
    raise SystemExit


class Ticket(object):

    def __init__(self, x, y, order,):
        self.length = (x[0], x[1])
        self.range = (y[0], y[1], y[2])
        self.rule = ([1, 2], [2, 59])
        self.order = order

    def __call__(self):

        def ball(length, _range, _low):
            ob = Ball(length, _range, _low)
            return ob.generate()

        logic = True

        if self.length[0] < 1 or self.length[0] > 6:
            logic = False
        if self.range[0] < self.length[0] or self.range[0] > 59:
            logic = False
        if self.length[0] < 1 or self.length[0] > 6 and self.range[1] > 1:
            logic = False

        if logic is True:

            check = True

            if self.length[1] + self.range[1] is 0:
                x = ball(self.length[0], self.range[0], self.range[2])
                return x

            if self.length[1] < 1 or self.length[1] > 2:
                check = False
            if self.range[1] < 2 or self.range[1] > 59:
                check = False

            if check is True:

                x = ball(self.length[0], self.range[0], self.range[2])
                y = ball(self.length[1], self.range[1], self.range[2])

                if self.order is True:
                    return sorted(x) + sorted(y)
                else:
                    return x + y
            else:
                raise Exception('Not A Lottery Type!')
        else:

            raise Exception('Not A Lottery Type!')
