class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #put numbers in a stack 
        #31 29 30 35

        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            
            curr = temperatures[i]

            #until greater num appears
            while stack and temperatures[stack[-1]] < curr:
                
                diff = i - stack[-1]
                result[stack[-1]] = diff
                stack.pop()
            
            stack.append(i)

        return result