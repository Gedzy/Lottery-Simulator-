#!/usr/bin/python
# -*- coding: utf-8 -*-


class Ball(object):
    def __init__(self, length, number, low):
        self.length = length
        self.number = number
        self.low = low
        self.path = '/dev/urandom'

    def randint(self, a, b):
        # Return random integer in range [a, b], including both end points.
        return a + self.randbelow(b - a + 1)

    def randbelow(self, value):

        length = value.bit_length()
        byte = (length + 7) // 8

        while True:

            rand = int.from_bytes(self.random_bytes(byte), 'little')
            rand >>= byte * 8 - length

            if rand < value:
                return rand

    def random_bytes(self, n):

        f = open(self.path, 'rb')

        try:
            with f as file:
                if f is not None:
                    return file.read(n)
        except KeyboardInterrupt:
            f.close()
            raise SystemExit
        finally:
            f.close()

    def generate(self):

        array = [0] * self.length

        index = 0

        for increment in range(len(array)):
            while index < self.length:
                stream = self.randint(self.low, self.number)
                if stream not in array:
                    array[index] = stream
                    index += 1
                del stream
        del index

        return array
