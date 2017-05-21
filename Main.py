#!/usr/bin/python
# -*- coding: utf-8 -*-

try:

    import os
    import argparse
    import sys

    from Lottery import Game

except KeyboardInterrupt:
    raise SystemExit


def main():

    os.environ['TERM'] = 'xterm'

    # Console interface using Argument parse package.
    parser = argparse.ArgumentParser(description='Lottery Simulator - Gedzy@live.co.uk')

    parser.add_argument('-l', nargs='?', help='Lotto')
    parser.add_argument('-e', nargs='?', help='Euro Millions')
    parser.add_argument('-t', nargs='?', help='Thunder Ball')
    parser.add_argument('-o', nargs='?', help='Hot Picks')
    parser.add_argument('-a', nargs='?', help='Health Lottery')
    parser.add_argument('-i', nargs='?', help='Irish Lotto')

    # Millionaire Maker, Millionaire Raffle and Postcode Lottery could be done in future updates.

    # Pack argument into a variable called args.
    args = parser.parse_args()

    def info():
        parser.print_help()
        parser.exit(1)

    def menu(n, arg):

        if arg is None:
            info()
        else:

            ob = None

            value = 0

            try:
                value = int(arg)
            except ValueError:
                info()

            if value > 0 and value <= 1000000000:
                ob = Game(n, value)
            else:
                info()

            ob.setup()

    if args.l:
        menu(1, args.l)
    elif args.e:
        menu(2, args.e)
    elif args.t:
        menu(3, args.t)
    elif args.o:
        menu(4, args.o)
    elif args.a:
        menu(5, args.a)
    elif args.i:
        menu(6, args.i)

    info()

if __name__ == '__main__':
        main()
