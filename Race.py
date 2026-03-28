import random

from graphics import *
from Dice import Dice
import time

class Horse:
    def __init__(self,speed,y,image,window):
        self.x = 50
        self.y = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        roll_value = self.dice.roll()
        self.x += roll_value

    def draw(self):
        try:
            self.image.undraw()
        except:
            pass
        self.image.draw_at_pos(self.window,self.x, self.y)
    def crossed_finish_line(self, finsih_x):
        return self.x >= finsih_x

def main():
    win = GraphWin("Horse Race", 700,700)
    try:
        win.autoflush = False
    except:
        pass
    horse1_img = Image(Point(0,0), "horse1_img.png")
    horse2_img = Image(Point(0,0), "horse2_img.png")
    horse3_img = Image(Point(0,0), "horse3_img.png")
    horse1 = Horse(random.randint(6,10),150, horse1_img, win)
    horse2 = Horse(random.randint(6,10),350, horse2_img, win)
    horse3 = Horse(random.randint(6,10), 550, horse3_img, win)
    finsh_x = 600
    finsh_line = Line(Point(finsh_x, 0), Point(finsh_x,700))
    horse1.draw()
    horse2.draw()
    horse3.draw()
    finsh_line.draw(win)
    win.getMouse()
    race_over = False
    while not race_over:
        if win.isClosed():
            break
        horse1.move()
        horse2.move()
        horse3.move()
        horse1.draw()
        horse2.draw()
        horse3.draw()
        try:
            update()
        except:
            pass
        h1 = horse1.crossed_finish_line(finsh_x)
        h2 = horse2.crossed_finish_line(finsh_x)
        h3 = horse3.crossed_finish_line(finsh_x)
        if h1 or h2 or h3:
            race_over = True
        time.sleep(0.06)
    if (h1 and h2) or (h1 and h3) or (h2 and h3):
        print("draw")
    elif h1:
        print("horse 1 win")
    elif h2:
        print("horse 2 win")
    elif h3:
        print("horse 3 win")

    try:
        win.getMouse()
    except:
        pass
    win.close()
if __name__ == "__main__":
    main()
