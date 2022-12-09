array = [[0, 1, 0, 0, 3, 0, 0, 6, 2],
         [0, 4, 0, 0, 0, 9, 0, 0, 0],
         [0, 0, 6, 4, 0, 0, 7, 0, 0],
         [0, 0, 0, 7, 0, 0, 9, 0, 6],
         [0, 5, 2, 0, 0, 0, 0, 8, 0],
         [3, 0, 0, 1, 8, 0, 0, 0, 0],
         [0, 0, 8, 2, 0, 5, 3, 0, 0],
         [0, 0, 1, 0, 6, 0, 0, 4, 0],
         [7, 0, 0, 0, 0, 0, 0, 9, 5]
         ]


class Sudoku:

    def __init__(self, target):
        self.rows = target

    def __show__(self):
        for i in range(9):
            print(self.rows[i])


s1 = Sudoku(array)
s1.__show__()


