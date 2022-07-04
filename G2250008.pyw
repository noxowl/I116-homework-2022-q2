#!/usr/bin/env python
# -*- coding: utf-8 -*-
# name: RHIE Suyeong
# id: 2250008
# acknowledgements: None
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Report Assignment

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)

Report Assignment: Game of Life
Use Tkinker to implement the Game of Life in Python.
Assume that an input grid is of rectangle shape and it is regarded as a flat torus.

Instructions on This Task:
- The program name must be GyourStudentID.pyw, like G2209999.pyw.
- The program must take a text file of an initial configuration.
- On lecturer’s environment your program will be executed by:
      py Gxxxxxxxxx.py glider.txt
      py Gxxxxxxxxx.py gosper.txt
      
Evaluation:
- +15 points if program runs on glider.txt at 􏳚 0.5 frame per second
- +15 points if program runs on gosper.txt at 􏳚 0.5 frame per second
- −10 points in case that flat torus model is not used
NB. possible total points are 30, 20, 15, 5, or 0 (no partial credits)

Submission:
submit by email
  Subject: report
      To: (check report slide 4p)@ml.jaist.ac.jp
attaching only one file: GyourStudentID.py.

code must start from information
    # name: your full name
    # id: your student ID
    # acknowledgements: name if anybody has assisted you
deadline: July 20 (Wed) 13:00 JST

Remark on Report Submission:
- deadline is strict (no deadline extension)
- submission style is strict, and do not submit any additional file
- use Python 3.10.*
- do not import any file/library except sys and tkinter
- program that ignores input file is evaluated to 0 points
- program is run on PC with Intel Core i7-1065G7 CPU 1.30GHz
- do not ask me to test your code
- no plagiarism: write every single letter by yourself in your understanding
    investigate by yourself what is regarded as plagiarism
"""
import sys
import tkinter


class GameOfLifeData:
    def __init__(self, seed):
        self.cells = []
        if seed:
            with open(seed, 'r') as f:
                for line in f:
                    line.rstrip('\n')
                    self.cells.append([l == '#' for l in line])
        self.rows = len(self.cells)
        self.row_index = self.rows - 1
        self.columns = len(self.cells[0] if self.cells else '')
        self.col_index = self.columns - 1


class GameOfLifeView:
    def __init__(self):
        self._root = tkinter.Tk()
        self._root.title('Report Assignment - 2250008 RHIE Suyeong')
        self._canvas = tkinter.Canvas(self._root)
        self._canvas.pack()
        self._dot_size = 20
        self._grid = {}
        self.buffer = []

    def _set_grid(self, rows, columns):
        for r in range(rows):
            self._grid.update({r: []})
            self.buffer.append([])
            for c in range(columns):
                x1, y1 = c * self._dot_size, r * self._dot_size
                x2, y2 = x1 + self._dot_size, y1 + self._dot_size
                self._grid[r].append(
                    self._canvas.create_rectangle(x1, y1, x2, y2, fill="#555"))
                self.buffer[r].append(False)

    def init_canvas(self, rows, columns):
        if rows and columns:
            self._canvas.config(
                width=columns * self._dot_size,
                height=rows * self._dot_size)
            self._set_grid(rows, columns)

    def _update_canvas(self):
        for ri in range(len(self.buffer)):
            for ci in range(len(self.buffer[ri])):
                if self.buffer[ri][ci]:
                    self._canvas.itemconfig(self._grid[ri][ci], fill="#f88")
                else:
                    self._canvas.itemconfig(self._grid[ri][ci], fill="#333")

    def on_update(self, f):
        self.buffer = f()
        self._update_canvas()
        self._root.after(100, self.on_update, f)


class GameOfLifeLogic:
    def __init__(self, view, data):
        self.view: GameOfLifeView = view
        self.data: GameOfLifeData = data
        self.view.init_canvas(self.data.rows, self.data.columns)

    def _safe_row_index(self, i: int):
        if i < 0:
            return self.data.row_index
        elif i > self.data.row_index:
            return 0
        else:
            return i

    def _safe_col_index(self, i: int):
        if i < 0:
            return self.data.col_index
        elif i > self.data.col_index:
            return 0
        else:
            return i

    def _check_cells(self):
        current = []
        for c in self.data.cells:
            current.append([x for x in c])
        for ri in range(len(self.data.cells)):
            prev_row = self._safe_row_index(ri - 1)
            next_row = self._safe_row_index(ri + 1)
            for ci in range(len(self.data.cells[ri])):
                prev_col = self._safe_col_index(ci - 1)
                next_col = self._safe_col_index(ci + 1)
                self.data.cells[ri][ci] = self._seek_cell(
                    self.data.cells[ri][ci],
                    (1 if current[prev_row][prev_col] else 0) +
                    (1 if current[prev_row][ci] else 0) +
                    (1 if current[prev_row][next_col] else 0) +
                    (1 if current[ri][prev_col] else 0) +
                    (1 if current[ri][next_col] else 0) +
                    (1 if current[next_row][prev_col] else 0) +
                    (1 if current[next_row][ci] else 0) +
                    (1 if current[next_row][next_col] else 0)
                    )

    def _seek_cell(self, alive, neighbors: int):
        if alive and neighbors < 2 or neighbors > 3:
            return False
        else:
            if not alive and neighbors == 3:
                return True
        return alive

    def update(self):
        self._check_cells()
        return self.data.cells

    def run(self):
        self.view._root.after(0, self.view.on_update, self.update)
        self.view._root.mainloop()


class GameOfLife:
    def __init__(self, payload):
        self.data = GameOfLifeData(payload)
        self.view = GameOfLifeView()
        self.logic = GameOfLifeLogic(self.view, self.data)

    def execute(self):
        self.logic.run()


if __name__ == '__main__':
    payload = sys.argv[-1]
    if payload.endswith('.txt'):
        gol = GameOfLife(payload)
        gol.execute()
    else:
        raise ValueError('No txt file found. Abort.')
