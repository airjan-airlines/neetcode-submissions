class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  "".join(char for char in s if char.isalnum())
        s = s.lower()
        i = 0
        while i < len(s) //2:
            if s[i] != s[-1-i]:
                return False
            i += 1        
        
        return True