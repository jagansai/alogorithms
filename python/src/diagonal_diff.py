

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# 1 2 3
# 4 5 6
# 7 8 9


def diagonalDifference(arr: List[int]):
    length = len(arr[0])

    def collect_diagonals(left_column, right_column):
        left_diagonal_sum : int = 0
        right_diagonal_sum : int = 0
        for i in range(0, length):
            left_diagonal_sum += arr[i][left_column]
            right_diagonal_sum += arr[i][right_column]
            left_column += 1
            right_column -= 1
        return (left_diagonal_sum, right_diagonal_sum)

    left_diagonal, right_diagonal = collect_diagonals(0, length - 1)
    return abs( left_diagonal - right_diagonal )


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
