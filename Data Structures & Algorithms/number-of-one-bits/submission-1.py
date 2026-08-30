class Solution:
    def hammingWeight(self, n: int) -> int:
        number = 0
        n=int(format(n, 'b'))
        for i in range(32):
            if n % 10 != 0:
                number += 1
            n = int(n//10)
            if n == 0:
                return number
        return number