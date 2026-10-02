class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = {'(':')', '{':'}', '[':']'}
        builder = []

        for i in range(len(s)):
            if s[i] in opening:
                builder.append(s[i])
            else: 
                if len(builder) < 1 or opening[builder.pop()] != s[i]:
                    return False

        return len(builder) == 0
        
