class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substr = set()
        l, r = 0, 0
        length = 0

        for i in range(len(s)):
            if s[i] not in substr: 
                substr.add(s[i])
                r = r + 1
            else:
                while s[i] in substr:
                    substr.remove(s[l])
                    l = l + 1
                
                substr.add(s[i])

            if len(substr) > length: 
                length = len(substr)
            
            print(substr)

        #while next letter not in set, put in set 

        return length


        