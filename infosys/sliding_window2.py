# sliding window in fixed size
# Maximum Sum of Distinct Subarrays With Length K
# You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k

# Driver code (no leading spaces)
nums = [1, 12, -5, -6, 50, 3]
k = 4

sol = Solution()
print(sol.findMaxAverage(nums, k))  # Output: 12.75
