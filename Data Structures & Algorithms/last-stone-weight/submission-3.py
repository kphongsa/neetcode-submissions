class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #make a max heap 

        stones = [-x for x in stones]
        heapq.heapify(stones)

        #pop the biggest two 

        while len(stones) > 1:
        
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if x == y: 
                continue
            elif x < y: 
                x = x - y
                heapq.heappush(stones, x)
            else: 
                y = y - x
                heapq.heappush(stones, y)

        if len(stones) == 0:
            return 0
        
        return heapq.heappop(stones) * -1

        