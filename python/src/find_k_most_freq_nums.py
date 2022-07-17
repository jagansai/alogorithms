"""
Find K most frequent numbers in the list.
"""

import bisect
from typing import Dict, List


def findKMostFreqNums(nums: List[int], k: int):
    num_freq: Dict[int, int] = dict()
    for num in nums:
        count = num_freq.get(num, 0) + 1
        num_freq[num] = count

    result = []
    for num_key in num_freq:
        bisect.insort(
            result, (num_key, num_freq[num_key]), key=lambda x: num_freq[num_key])

    return (x for x in result[:k])


if __name__ == '__main__':
    for (num, count) in findKMostFreqNums([1, 2, 3, 4, 1, 2, 3, 1, 2, 4, 3, 1, 2, 1], 3):
        print(f"{num}: {count} times repeated")
