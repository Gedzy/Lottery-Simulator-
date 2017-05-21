#!/usr/bin/python
# -*- coding: utf-8 -*-

try:

    from curses import wrapper, initscr, endwin
    from time import sleep

except KeyboardInterrupt:
    raise SystemExit


class Messenger(object):

    # Object instantiation...
    def __init__(self):
        self.window = initscr()

    @classmethod
    def run(cls, obj):
        wrapper(obj)

    @classmethod
    def update(cls, screen, wait, message):
        screen.addstr(0, 0, message)
        screen.refresh()
        sleep(wait)

    @classmethod
    def stop(cls):
        endwin()
