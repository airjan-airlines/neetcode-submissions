class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(re.sub(r'[\W_]', '', s).lower())
        while len(s) > 1:
            if not s.pop(0) == s.pop():
                return False

        return True