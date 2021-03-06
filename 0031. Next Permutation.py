class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] < nums[idx + 1]:
                break
            idx -= 1
        
        if idx < 0:
            nums[:] = nums[::-1]
            return 
        
        nextIdx = idx + 1
        while nextIdx < len(nums) and nums[nextIdx] > nums[idx]:
            nextIdx += 1
        
        nums[idx], nums[nextIdx - 1] = nums[nextIdx - 1], nums[idx] 
        nums[idx+1:] = nums[idx+1:][::-1]