from ast import Num
from collections import namedtuple
import enum
import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


class NumCat(enum.Enum):
    pos = 1
    neg = -1
    zero = 0


def plusMinus(arr: List[int]):

    def get_enum(val: int) -> NumCat:
        if val > 0:
            return NumCat.pos
        elif val < 0:
            return NumCat.neg
        else:
            return NumCat.zero

    length = len(arr)
    pos_neg_zero_dict = dict()
    for num in arr:
        num_cat = get_enum(num)
        total_value = pos_neg_zero_dict.get(num_cat, 0)
        total_value += 1
        pos_neg_zero_dict[num_cat] = total_value

    for num_cat in [NumCat.pos, NumCat.neg, NumCat.zero]:
        print("{:.6f}".format(pos_neg_zero_dict.get(num_cat, 0) / length))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
