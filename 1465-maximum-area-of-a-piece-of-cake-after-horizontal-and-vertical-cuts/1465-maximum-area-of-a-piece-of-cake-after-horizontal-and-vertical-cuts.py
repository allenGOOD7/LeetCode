class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        curr_horizon = 0
        curr_vertical = 0    
        
        max_height = 0
        for i in horizontalCuts:
            max_height = max(i - curr_horizon, max_height)
            curr_horizon = i
        
        max_width = 0
        for i in verticalCuts:
            max_width = max(i - curr_vertical, max_width)
            curr_vertical = i
            
        return (max_height * max_width) % (10**9+7)