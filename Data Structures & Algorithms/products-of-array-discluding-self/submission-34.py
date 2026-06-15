class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []

        for i in range(len(nums)):
            if (i == 0):
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])

        for i in range(len(nums), 0, -1):
            if (i == len(nums)): 
                suffix.append(1)
            else: 
                suffix.insert(0, suffix[0] * nums[i])

        for i in range(len(nums)): 
            output.append(prefix[i] * suffix[i])

        return output

        