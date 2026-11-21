# Find Pivot Index

""" Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1. """

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right = sum(nums)
        left = 0

        for i in range(n):
            right -= nums[i]
            
            if left == right:
                return i
            
            left += nums[i]

        return -1


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Pivot at index 3 (left sum = 1+7+3 = 11, right sum = 5+6 = 11)
    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
    
    # Example 2: No pivot index exists
    print(sol.pivotIndex([1, 2, 3]))           # Output: -1
    
    # Example 3: Pivot at index 0 (left sum = 0, right sum = 1 + -1 = 0)
    print(sol.pivotIndex([2, 1, -1]))          # Output: 0
