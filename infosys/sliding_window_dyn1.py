# Longest Substring with At Most K Distinct Characters

# sliding window in Dynamic

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
            
        n = len(s)
        basket = {}
        left = 0
        max_char = 0

        for right in range(n):
            basket[s[right]] = basket.get(s[right], 0) + 1

            while len(basket) > k:
                basket[s[left]] -= 1
                if basket[s[left]] == 0:
                    del basket[s[left]]
                left += 1

            max_char = max(max_char, right - left + 1)
            
        return max_char


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "ece" has length 3 with k = 2 distinct characters
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))  # Output: 3
    
    # Example 2: "aa" has length 2 with k = 1 distinct character
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))     # Output: 2
    
    # Example 3: Edge case when k = 0
    print(sol.lengthOfLongestSubstringKDistinct("abc", 0))    # Output: 0
