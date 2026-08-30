class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # simple check before looping / doing more costly checks
        if len(s) != len(t): 
            return False

        if set(s) != set(t): # checks letter distinction but fails at length
            return False;

        s_dict = {}
        t_dict = {}

        # we already know that they are the same length
        for i in range(len(s)) :
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1
            s_dict[s[i]] += 1

            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 1
            t_dict[t[i]] += 1
        
        if s_dict != t_dict:
            return False
        return True