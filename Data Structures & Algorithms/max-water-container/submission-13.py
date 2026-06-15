class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        area = (right - left) * min(heights[left], heights[right])

        while left < right: 
            new_area = (right - left) * min(heights[left], heights[right])
            area = max(area, new_area)

            if heights[left] < heights[right]: 
                left = left + 1
            else: 
                right = right - 1
 
            
        return area




        