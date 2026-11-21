# Prefix_Sum Problem

#Subarray Sums Divisible by K

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5

Output: 7

Explanation: There are 7 subarrays with a sum divisible by k = 5:

[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9

Output: 0 

"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = {0: 1}
        pref_sum = 0
        rem = 0
        count = 0

        for num in nums:
            pref_sum += num

            rem = pref_sum % k

            if rem in table:
                count += table[rem]

            table[rem] = table.get(rem, 0) + 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # Output: 7
