class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        product = []

        for i in range(len(nums)):
            prefix.append(nums[i] * prefix[i])
        
        for i in range(len(nums)):
            suffix.append(nums[-i-1] * suffix[i])

        for i in range(len(nums)):
            product.append(prefix[i] * suffix[len(nums) - i - 1])
        
        return product