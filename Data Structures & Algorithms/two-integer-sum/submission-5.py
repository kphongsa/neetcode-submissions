class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
            
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in num_map: 
                return [num_map[compliment], i]
            else:
                num_map[nums[i]] = i

        return []
            