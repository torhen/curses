import curses
import datetime
import random

class App:
    def __init__(self, win):
        self.win = win
        self.xmax = 80
        self.ymax = 25
        self.doc = []
        for y in range(self.ymax):
            self.doc.append([])
            for x in range(self.xmax):
                self.doc[y].append('*' * self.xmax)
        self.win.nodelay(True)
        self.run()

    def update(self):
        for y in range(self.ymax):
            for x in range(self.xmax):
                self.doc[y][x] = random.choice('abcdeghijklmnopqurstuvxyz      ')
        s = str(datetime.datetime.now())
        self.doc[0][0:len(s)] = s

    def draw(self):

        inp = self.win.getch()
        if inp != curses.KEY_RESIZE:
                self.win.clear()
                

        height, width = self.win.getmaxyx()
        for y in range(height-1):
            for x in range(width-1):
                if y < self.ymax and x < self.xmax:
                    self.win.addstr(y, x, self.doc[y][x])
                else:
                    self.win.addstr(y, x, ' ')
        self.win.refresh()

    def run(self):
        while True:
            self.update()
            self.draw()



def main(win):
    App(win)

curses.wrapper(main)
