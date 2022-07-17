import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n: int):
    # Write your code here
    
    stair = '#'
    for i in range(1, n + 1):
        print((i * stair).rjust(n))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
