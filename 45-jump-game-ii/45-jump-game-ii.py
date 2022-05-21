class Solution:
    def jump(self, nums: List[int]) -> int:       
        jumpPoint = 0
        maxReach = 0
        steps = 0
        
        for i in range(len(nums)-1):
            maxReach = max(i + nums[i], maxReach)
            if i == jumpPoint:
                steps += 1
                jumpPoint = maxReach
        return steps
        