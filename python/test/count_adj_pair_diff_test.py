
from src.count_adjacent_pair_with_diff import count_adjacent_pairs_with_same_diff

def test_count_adj_pair():
    result = count_adjacent_pairs_with_same_diff( [1, 2, 3, 5, 7, 6, 9, 12 ] )
    
    assert( result == { 1: [(1, 2), (2, 3), (7,6)], 2: [(3, 5), (5, 7)], 3: [(6, 9), (9,12)] } )