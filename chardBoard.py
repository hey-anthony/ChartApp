from tkinter import *


class NetXY:
    """Класс координатной сетки"""

    def __init__(self, xSize, ySize, step):
        """Конструктор сетки"""
        self.xSize = xSize
        self.ySize = ySize
        self.step = step
        self.countX = xSize // step
        self.countY = ySize // step
        self.board = Tk()
        self.board.geometry(str(self.xSize) + 'x' + str(self.ySize))
        self.canvas = Canvas(self.board, width=xSize, height=ySize, bg='#002')
        pass

    # метод построение сетки
    def buildNet(self):
        for i in range(self.countY):
            self.canvas.create_line(0, i * self.step, self.xSize, i * self.step, width=1, fill='black')

        for i in range(self.countX):
            self.canvas.create_line(i * self.step, 0, i * self.step, self.ySize, width=1, fill='black')

        centerX = self.countY // 2 * self.step
        centerY = self.countX // 2 * self.step
        self.canvas.create_line(0, centerX, self.xSize, centerX, width=2, arrow=LAST, fill='white')
        self.canvas.create_line(centerY, 0, centerY, self.ySize, width=2, arrow=FIRST, fill='white')

        return self.canvas.pack(), self.board.mainloop()

    # метод построение осей X Y
    def axisXY(self):
        self.canvas.create_line(0, self.ySize // 2, self.xSize, self.ySize // 2, width=2, arrow=FIRST, fill='white')
        self.canvas.create_line(self.xSize // 2, 0, self.xSize // 2, self.ySize, width=2, arrow=LAST, fill='white')
        return self.canvas.pack(), self.board.mainloop()
