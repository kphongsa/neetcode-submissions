class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #add numbers till it works? n^2
        #if a sum is smaller / larger, don't need to try sums smaller / larger
        #array is sorted? 

        #two pointers
        length = len(numbers)
        left = 0
        right = length - 1

        while numbers[left] + numbers[right] != target: 
            if numbers[left] + numbers[right] > target: 
                right = right - 1 
            else: 
                left = left + 1
            
        return [left + 1, right + 1]
                
