class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest_seen = 0

        while left <= len(s) and longest_seen < len(s) - left:
            while right < len(s) and not s[right] in s[left:right]:
                right += 1
            if right - left > longest_seen:
                longest_seen = right - left
            left += 1

        return longest_seen
