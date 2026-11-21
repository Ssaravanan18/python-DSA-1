# Prefix Sum
# Subarray Sum Equals K

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2

Output: 2

Example 2:
Input: nums = [1,2,3], k = 3

Output: 2 """
"""
Problem	Initialisation
Longest Subarray Sum K	{0: -1}
Subarray Sum Equals K (560)	{0: 1}
Subarray Sums Divisible by K (974)	{0: 1}"""


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0: 1}  # stores frequency of each prefix sum seen so far
        pref_sum = 0
        count = 0

        for num in nums:
            pref_sum += num
            target_pref = pref_sum - k

            if target_pref in table:
                count += table[target_pref]

            table[pref_sum] = table.get(pref_sum, 0) + 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))     # Expected: 2 ([1,1] twice)
    print(sol.subarraySum([1, 2, 3], 3))     # Expected: 2 ([1,2] and [3])
    print(sol.subarraySum([1, -1, 0], 0))    # Expected: 3 ([1,-1], [0], and [1,-1,0])
