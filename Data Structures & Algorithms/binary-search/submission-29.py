class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
        
        while r - l >= 0:
            i = (r-l)//2 + l

            if (target == nums[i]):
                return i
            elif (r == l and target != nums[i]):
                return -1
            elif (target < nums[i]):
                r = i
            elif (target > nums[i]):
                l = i + 1

        return -1
        
        
