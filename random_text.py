import curses
import datetime
import random
import time

class App:
    def __init__(self, win):
        self.win = win
        self.xmax = 80
        self.ymax = 25
        self.doc = []
        for y in range(self.ymax):
            self.doc.append([])
            for x in range(self.xmax):
                self.doc[y].append(' ' * (self.xmax-1))
        self.win.nodelay(True)
        self.run()

    def update(self):
       
        for y in range(self.ymax-1, 0, -1):
             for x in range(self.xmax):
                self.doc[y][x] = self.doc[y-1][x]

        for x in range(self.xmax):
            self.doc[0][x] = random.choice('abcdefghijklmnopqrstuvwxyz      ')


    def draw(self):

        inp = self.win.getch()
        if inp != curses.KEY_RESIZE:
                self.win.clear()

        height, width = self.win.getmaxyx()
        for y in range(height-2):
            for x in range(width-2):
                if y < self.ymax and x < self.xmax:
                    self.win.addstr(y, x, self.doc[y][x])
                else:
                    self.win.addstr(y, x, ' ')
        self.win.refresh()
        time.sleep(0.5)

    def run(self):
        while True:
            self.update()
            self.draw()



def main(win):
    App(win)

curses.wrapper(main)
