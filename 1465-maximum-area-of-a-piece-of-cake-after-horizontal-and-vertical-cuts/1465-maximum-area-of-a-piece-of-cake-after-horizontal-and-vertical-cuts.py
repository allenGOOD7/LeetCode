class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        curr_horizon = 0
        curr_vertical = 0
#         max_area = 0
        
#         for i in horizontalCuts:
#             curr_vertical = 0
#             for j in verticalCuts:
#                 area = (i - curr_horizon) * (j - curr_vertical)
#                 if area >= h * w / 2:
#                     return area % (10**9 + 7)
#                 max_area = max(max_area, area)
#                 curr_vertical = j
#             curr_horizon = i
#         return max_area % (10**9 + 7)
    
        
        max_height = 0
        for i in horizontalCuts:
            max_height = max(i - curr_horizon, max_height)
            curr_horizon = i
        
        max_width = 0
        for i in verticalCuts:
            max_width = max(i - curr_vertical, max_width)
            curr_vertical = i
            
        return (max_height * max_width) % (10**9+7)