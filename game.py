import numpy as np
import random

class TwentyFortyEight:
    def __init__(self):
        self.matrix = np.zeros((4, 4), dtype=int)  # Initialize with integers
        count = 0
        while count < 2:
            matrix_col = random.randrange(0, 4)
            matrix_row = random.randrange(0, 4)
            if self.matrix[matrix_row][matrix_col] == 0:
                num = int(2)
                if random.randrange(0, 11) == 10:
                    num = int(4)
                self.matrix[matrix_row][matrix_col] = num
                count += 1

    def insert_num(self):
        while True:
            matrix_col = random.randrange(0, 4)
            matrix_row = random.randrange(0, 4)
            if self.matrix[matrix_row][matrix_col] == 0:
                num = int(2)
                if random.randrange(0, 11) == 10:
                    num = int(4)
                self.matrix[matrix_row][matrix_col] = num
                break

    def move_h(self, n: int):
        for i in range(0, 4):
            beg, end = 0, 1
            if n == -1:
                beg, end = 3, 2
            while min(beg, end) >= 0 and max(beg, end) < 4:
                if self.matrix[i][beg] != 0:
                    beg += n
                    end = max(end, beg + n)
                    if n == -1:
                        end = min(end, beg + n)
                elif self.matrix[i][end] != 0:
                    self.matrix[i][beg] = self.matrix[i][end]
                    self.matrix[i][end] = 0
                    beg += n
                    end += n
                else:
                    end += n

    def move_v(self, n: int):
        for j in range(0, 4):
            beg, end = 0, 1
            if n == -1:
                beg, end = 3, 2
            while min(beg, end) >= 0 and max(beg, end) < 4:
                if self.matrix[beg][j] != 0:
                    beg += n
                    end = max(end, beg + n)
                    if n == -1:
                        end = min(end, beg + n)
                elif self.matrix[end][j] != 0:
                    self.matrix[beg][j] = self.matrix[end][j]
                    self.matrix[end][j] = 0
                    beg += n
                    end += n
                else:
                    end += n

    def horizontal(self, n: int) -> bool:
        m = self.matrix.copy()
        beg, end = 0, 3
        if n == -1:
            beg, end = end, beg
        for i in range(0, 4):
            for j in range(beg, end, n):
                if self.matrix[i][j] != 0:
                    for k in range(j, end + n, n):
                        if j != k and self.matrix[i][k] != 0:
                            if self.matrix[i][j] == self.matrix[i][k]:
                                self.matrix[i][j] *= 2
                                self.matrix[i][k] = 0
                            break
        self.move_h(n)
        if not np.array_equal(m, self.matrix):
            self.insert_num()
        return (m != self.matrix).all()

    def vertical(self, n: int) -> bool:
        m = self.matrix.copy()
        beg, end = 0, 3
        if n == -1:
            beg, end = end, beg
        for j in range(0, 4):
            for i in range(beg, end, n):
                if self.matrix[i][j] != 0:
                    for k in range(i, end + n, n):
                        if i != k and self.matrix[k][j] != 0:
                            if self.matrix[i][j] == self.matrix[k][j]:
                                self.matrix[i][j] *= 2
                                self.matrix[k][j] = 0
                            break
        self.move_v(n)
        if not np.array_equal(m, self.matrix):
            self.insert_num()
        return (m != self.matrix).all()
