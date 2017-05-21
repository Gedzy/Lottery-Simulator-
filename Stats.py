#!/usr/bin/python
# -*- coding: utf-8 -*-


class Stats(object):

    def __init__(self, ticket, draw, matcher, winnings, length, differ):

        self.ticket = ticket      # [x, x, x, x, x]
        self.draw = draw          # [y, y, y, y, y]
        self.matcher = matcher    # 2, 0 = 3.30
        self.winnings = winnings  # Checked against matcher
        self.length = length      # Length of Ticket/Array
        self.differ = differ      # 50, 12 = [5, 1 and 50] - [2, 1, and 12]

        self.a_cost = 0
        self.a_return = 0

        self.a_purchase = 0
        self.a_percentage = 0

        self.a_maximum_number = [0] * self.differ[0]  # Most Common Number _ Array
        self.a_maximum_special = [0] * self.differ[1]  # Star

        self.a_minimum_number = [0] * self.differ[0]  # Least Common Number _ Array
        self.a_minimum_special = [0] * self.differ[1]

    def the_ticket(self):
        return self.py_replace(self.ticket, '[', '', ']', '')

    def the_draw(self):
        return self.py_replace(self.draw, '[', '', ']', '')

    def the_cost(self, float_value):
        self.a_cost += float_value
        del float_value
        return self.py_format('£{0:.2f}p', self.a_cost)

    def the_return(self):
        self.a_return += self.array_payout()
        return self.py_format('£{0:.2f}p', self.a_return)

    def the_profit(self):
        return self.py_format('£{0:.2f}p', self.a_return - self.a_cost)

    def the_purchase(self):
        self.a_purchase += 1
        return self.a_purchase

    def the_percentage(self):

        ap = self.array_payout()

        if ap > 0.0:
            self.a_percentage += 1

        ratio = self.a_percentage / self.a_purchase * 100

        return self.py_format('£{0:.2f}%', ratio)

    def the_number(self):
        cn = self.the_maximum_number(), self.the_minimum_number()
        return self.py_replace(cn, '(', '', ')', '')

    def the_special(self):
        cs = self.the_maximum_special(), self.the_minimum_special()
        return self.py_replace(cs, '(', '', ')', '')

    def the_maximum_number(self):
        return self.array_count(0, self.a_maximum_number, 0, self.length[0])

    def the_maximum_special(self):
        return self.array_count(0, self.a_maximum_special, self.length[0], self.length[0] + self.length[1])

    def the_minimum_number(self):
        return self.array_count(1, self.a_minimum_number, 0, self.length[0])

    def the_minimum_special(self):
        return self.array_count(1, self.a_minimum_special, self.length[0], self.length[0] + self.length[1])

    def the_match(self):

        mba = self.array_match()

        if len(mba) is 0:
            mba = [0, 0]

        return self.py_replace(mba, '[', '', ']', '')

    def array_won(self):

        if self.array_payout() > 0.0:
            return 1
        else:
            return 0

    def array_match(self):

        ticket = [self.ticket[:self.length[0]], self.ticket[self.length[0]:self.length[0] + self.length[1]]]
        draw = [self.draw[:self.length[0]], self.draw[self.length[0]:self.length[0] + self.length[1]]]

        t_array = []
        d_array = []

        index_a = 0

        while index_a <= 1:
            index_b = 0
            for element in ticket[index_a]:
                index_b += 1
                if element in draw[index_a]:
                    if index_a == 0:
                        t_array.append([element, index_b])
                    if index_a == 1:
                        d_array.append([element, index_b + self.length[0]])

            index_a += 1

        tda = t_array + d_array

        del index_a, t_array, d_array

        return tda

    def array_payout(self):

            ap = self.array_match()

            element = []
            index = []

            for n in range(len(ap)):
                if ap[n][1] <= self.length[0]:
                    element.append(ap[n][0])
                elif ap[n][0] > self.length[0]:
                    index.append(ap[n][0])

            del ap

            value = 0.00

            for n in range(0, len(self.matcher)):
                if len(element) is self.matcher[n][0] and len(index) is self.matcher[n][1]:
                    value = self.winnings[n][0]

            del element, index

            return value

    def array_count(self, option, container, start, end):

        ac = self.ticket[start:end]

        if option is 0:

            most = [0] * len(ac)

            for i in range(len(ac)):
                most[i] = ac[i]
                container[most[i] - 1] += 1

            maximum = max(container)
            ac = 0

            for i in range(len(container)):
                if container[i] is maximum:
                    ac = i + 1

            del most, container, maximum

            return ac

        else:

            least = [0] * len(ac)

            for i in range(len(ac)):
                least[i] = ac[i]
                container[least[i] - 1] += 1

            minimum = min(container)
            ac = 0

            for i in range(len(container)):
                if container[i] is minimum:
                    ac = i + 1

            del least, container, minimum

            return ac

    @classmethod
    def py_replace(cls, data, s1, s2, s3, s4):
        return str(data).replace(s1, s2).replace(s3, s4)

    @classmethod
    def py_format(cls, string, data):
        return str(string).format(data)
