
# count how many adjacent pairs we have in an array with same difference.
## [1, 2, 3, 5, 7, 6, 9, 12 ]
## { 1: [(1, 2), (2, 3), (7,6)], 2: [(3, 5), (5, 7)], 3: [(6, 9), (9,12)] }

from typing import List, Dict, Tuple


def count_adjacent_pairs_with_same_diff(nums: List[int]) -> Dict[int, List[Tuple[int, int]]]:
    result_pairs: Dict[int, List[Tuple[int, int]]] = dict()

    for pair in zip(nums, nums[1:]):
        diff = abs(pair[0] - pair[1])
        list_of_pairs = result_pairs.get(diff, [])
        list_of_pairs.append((pair[0], pair[1]))
        result_pairs[diff] = list_of_pairs

    return result_pairs
