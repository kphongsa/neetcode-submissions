class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxl = 0
        l = 0

        for i in range(len(s)):
            if s[i] not in freq: 
                freq[s[i]] = 1
                maxl = max(maxl, i - l + 1)
            else: 
                while s[i] in freq: 
                    del freq[s[l]]
                    l = l + 1
                
                freq[s[i]] = 1
            
            
        
        return maxl


                

