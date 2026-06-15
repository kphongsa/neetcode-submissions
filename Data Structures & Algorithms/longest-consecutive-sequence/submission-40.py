class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: 
                return 0

        num_set = set(nums)

        max_length = 1
        start = 0

        for i in range(len(nums)): 
            if nums[i]-1 not in num_set and nums[i]+1 in num_set:
                start = nums[i]
            else:
                continue
            
            longest_set = set()
            longest_set.add(start)

            while start+1 in num_set: 
                start = start + 1
                longest_set.add(start)
                
                max_length = max(max_length, len(longest_set))

        return max_length

        