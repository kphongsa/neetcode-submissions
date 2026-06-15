class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []

        #first sort the array
        for i in range(len(nums)):
            j = i

            while(j > 0 and nums[j] < nums[j-1]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j = j-1

        #same as finding the target for two pairs
        #for i in nums: 
            #i will be the target, we want to find two pairs equal to i
        print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i] * -1

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]

                if (sum < target): 
                    left = left + 1
                elif (sum > target): 
                    right = right - 1
                else: 
                    trips.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
        return trips

        
