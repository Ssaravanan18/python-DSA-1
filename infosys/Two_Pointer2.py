# Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = 0

        while left <= right:
            # If the lightest and heaviest person can share a boat, board both
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always boards a boat
            right -= 1
            boat += 1

        return boat


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: (1, 2) -> 1 boat
    print(sol.numRescueBoats(, 3))        # Output: 1
    
    # Example 2: (1, 2), (2), (3) -> 3 boats
    print(sol.numRescueBoats(, 3))     # Output: 3
    
    # Example 3: (3), (3), (4), (5) -> 4 boats
    print(sol.numRescueBoats(, 5))     # Output: 4
