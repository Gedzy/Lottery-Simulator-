#!/usr/bin/python
# -*- coding: utf-8 -*-

try:

    from Ticket import Ticket
    from Stats import Stats
    from Messenger import Messenger
    from Ball import Ball

except KeyboardInterrupt:
    raise SystemExit


class Game(object):

    def __init__(self, op, nop):
        self.op = op
        self.nop = nop

    def setup(self):

        if self.op is 1:

            lo = Lottery()
            lo.nop(self.nop)
            lo.name('Lotto')
            lo.cost(0.285)  # x7 = £2 per 7 lines
            lo.length(6, 1)
            lo.differ(59, 59, 1)
            lo.matcher([[3, 0], [4, 0], [5, 0], [5, 1], [6, 0]])
            lo.winnings([[25.00], [100.00], [1000.00], [50000.00], [18700000.00]])
            lo.order(True)
            lo.draw()
            lo.ticket()
            lo.word('Bonus:     ')
            lo.run()

        if self.op is 2:

            em = Lottery()
            em.nop(self.nop)
            em.name('Euro Millions')
            em.cost(1.65)
            em.length(5, 2)
            em.differ(50, 12, 1)
            em.matcher([[2, 0], [2, 1], [1, 2], [3, 0], [3, 1], [2, 2], [4, 0], [3, 2], [4, 1], [4, 2], [5, 0], [5, 1],
                        [5, 2]])
            em.winnings([[3.30], [6.00], [7.60], [9.00], [10.70], [14.20], [43.30], [78.00], [123.00], [2307.00],
                        [190000000.00]])
            em.order(True)
            em.draw()
            em.ticket()
            em.word('Star:      ')
            em.run()

        if self.op is 3:

            tb = Lottery()
            tb.nop(self.nop)
            tb.name('Thunder Ball')
            tb.cost(1.00)
            tb.length(5, 1)
            tb.differ(39, 14, 1)
            tb.matcher([[0, 1], [1, 1], [2, 1], [3, 0], [4, 0], [4, 1], [5, 0], [5, 1]])
            tb.winnings([[3.00], [5.00], [10.00], [20.00], [100.00], [250.00], [5000.00], [500000.00]])
            tb.order(True)
            tb.draw()
            tb.ticket()
            tb.word('Ball:      ')
            tb.run()

        if self.op is 4:

            hp = Lottery()
            hp.nop(self.nop)
            hp.name('Hot Picks')
            hp.cost(1.00)
            hp.length(6, 0)
            hp.differ(59, 0, 1)
            hp.matcher([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]])
            hp.winnings([[6.00], [60.00], [800.00], [13000.00], [350000.00]])
            hp.order(True)
            hp.draw()
            hp.ticket()
            hp.word('')
            hp.run()

        if self.op is 5:

            hl = Lottery()
            hl.nop(self.nop)
            hl.name('Health Lottery')
            hl.cost(1.00)
            hl.length(5, 1)
            hl.differ(50, 50, 1)
            hl.matcher([[2, 1], [3, 0], [3, 1], [4, 0], [4, 1], [5, 0]])
            hl.winnings([[10.00], [20.00], [50.00], [250.00], [10000.00], [100000.00]])
            hl.order(True)
            hl.draw()
            hl.ticket()
            hl.word('Bonus:     ')
            hl.run()

        if self.op is 6:

            il = Lottery()
            il.nop(self.nop)
            il.name('Irish Lotto')
            il.cost(2.00)
            il.length(6, 1)
            il.differ(47, 47, 1)
            il.matcher([[2, 1], [3, 0], [3, 1], [4, 0], [4, 1], [5, 0], [5, 1], [6, 0]])
            il.winnings([[2.00], [7.00], [18.00], [36.00], [110.00], [1100.00], [73000.00], [1400000.00]])
            il.order(True)
            il.draw()
            il.ticket()
            il.word('Bonus:     ')
            il.run()


class Lottery(object):

    def __init__(self):

        # Lottery == Array
        # Formation = X and Y are processed to make Lottery Z
        # Lottery Z is now a Formation of the Euro Millions

        self.nop = self.nop

        self.name = self.name
        self.cost = self.cost  # 2.50 Maker Entry

        self.length = self.length  # Lottery X
        self.differ = self.differ  # Lottery Y
        self.order = self.order

        self.draw = self.draw
        # Draw ~ Process Lottery X and Y to Ticket Class
        self.ticket = self.ticket
        # Ticket ~ Process Lottery X and Y to Ticket Class

        self.matcher = self.matcher

        self.winnings = self.winnings

        self.word = self.word

        self.text = ['Playing:   ',
                     'Brought:   ',
                     'Spent:     ',
                     'Won:       ',
                     'Profit?:   ',
                     'W/L:       ',
                     'Ball:      ',
                     '',
                     'Match?:    ',
                     'Draw:      ',
                     'Ticket     ']

    def nop(self, n):
        self.nop = n

    def name(self, name):
        self.name = name

    def cost(self, amount):
        self.cost = amount

    def length(self, number, extra):
        self.length = number, extra

    def differ(self, low, high, lh):
        self.differ = low, high, lh

    def order(self, boolean):
        self.order = boolean

    def matcher(self, data):
        self.matcher = data

    def winnings(self, data):
        self.winnings = data

    def draw(self):
        self.draw = Ticket(self.length, self.differ, self.order)

    def ticket(self):
        self.ticket = Ticket(self.length, self.differ, self.order)

    def word(self, string):
        self.word = string

    def run(self):

        def simulation():

            i = self.nop

            self.text[7] = self.word
            gms = ''

            gtd = self.draw()

            get = Stats(self.ticket(), gtd, self.matcher, self.winnings, self.length, self.differ)

            while i is not 0:

                gtt = self.ticket()
                get.ticket = gtt

                gtp = get.the_purchase()
                gtc = get.the_cost(self.cost)
                gtr = get.the_return()
                gto = get.the_profit()
                gte = get.the_percentage()
                gtn = get.the_number()
                gtd = get.the_draw()
                gtt = get.the_ticket()

                if self.length[1] > 0:

                    gms = get.the_special()

                gmb = get.the_match()

                data = [self.name, gtp, gtc, gtr, gto, gte, gtn, gms, gmb, gtd, gtt]

                to = '\n%s%s\n\n%s%s\n%s%s\n\n%s%s\n%s%s\n%s%s\n\n%s%s\n%s%s\n\n%s%s\n\n%s%s\n%s%s\n\n'

                console.update(console.window, 0, to % (self.text[0], data[0],
                                                        self.text[1], data[1],
                                                        self.text[2], data[2],
                                                        self.text[3], data[3],
                                                        self.text[4], data[4],
                                                        self.text[5], data[5],
                                                        self.text[6], data[6],
                                                        self.text[7], data[7],
                                                        self.text[8], data[8],
                                                        self.text[9], data[9],
                                                        self.text[10], data[10]))

                if gtd == gtt:
                    exit()

                i -= 1

        console = Messenger()

        try:

            console.run(simulation())

        except (KeyboardInterrupt, TypeError):
            console.stop()
            raise SystemExit
        else:
            console.stop()
