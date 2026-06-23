class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        
        #counting partitions?
        
        if n in self.cache:
            return self.cache[n]

        if n == 1:
            result = 1
            self.cache[n] = result

            return result

        if n == 2:
            result = 2
            self.cache[n] = result

            return result

        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = result

        return result
