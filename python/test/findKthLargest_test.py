from src.findKthLargest import Solution


def testfindKthLargestElement():
    solution = Solution()
    assert solution.findKthLargest([1, 2, 4, 3, 5], 2) == 4
    assert solution.findKthLargest([1,2, 3, 4, 5, 6], 3 ) == 4
