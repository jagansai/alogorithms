

from src.diagonal_diff import diagonalDifference


def test_diagonal_diff():
    # 1 3 5
    # 2 5 7
    # 4 7 9
    # result = 1
    
    #  1  3  5
    # -2 -5 -7
    #  4  7  9
    # result = 1
    
    input_arr = [[1, 3, 5], [2, 5, 7], [4, 7, 9]]
    assert( diagonalDifference(input_arr) == 1 )
    
    input_arr = [[1, 3, 5], [-2, -5, -7], [4, 7, 9]]
    assert( diagonalDifference(input_arr) == 1)