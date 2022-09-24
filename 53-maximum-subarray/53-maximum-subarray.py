class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_num = max_num = nums[0]
        for num in nums[1:]:
            curr_num = max(num, curr_num + num)
            max_num = max(curr_num, max_num)
        return max_num