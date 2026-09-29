class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in count: 
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            if count[s[r]] > maxf:
                maxf = count[s[r]]
            
            

            res = r - l + 1
            if res - maxf > k: 
                count[s[l]] -= 1
                l = l + 1
                res = res - 1

            #print(count, res)
            
        return res