class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #find the cut, from the greatest to smallest element 
        #find cut by comparing mid to left and right

        l, r = 0, len(nums)-1 
        
        while r - l >= 1:
            
            mid = (l+r) // 2
            print(l, mid, r)

            #how does left compare to mid?

                #if left < mid: 
                    #left to mid in sorted order
                    
                #if left > mid: 
                    #cut is between left and mid 

            #how does right compare to mid? 

                #if right < mid
                    #cut is between mid and right

                #if right > mid 
                    #mid to right in sorted order


            if nums[l] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                return nums[l]
        
        return nums[l]