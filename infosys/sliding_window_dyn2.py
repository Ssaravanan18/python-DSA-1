# Fruit Into Baskets
# sliding windows in dynamic

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(n):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Pick from all 3 trees -> Output: 3
    print(sol.totalFruit([1, 2, 1]))           # Output: 3
    
    # Example 2: Pick from [1, 2, 2] -> Output: 3
    print(sol.totalFruit([0, 1, 2, 2]))        # Output: 3
    
    # Example 3: Pick from [2, 3, 2, 2] -> Output: 4
    print(sol.totalFruit([1, 2, 3, 2, 2]))     # Output: 4
