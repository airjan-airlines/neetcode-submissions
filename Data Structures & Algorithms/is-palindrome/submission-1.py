class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = list(s.lower())
        while len(s) > 1:
            if not s.pop(0) == s.pop():
                return False

        return True