from msilib.schema import Class


class Solution:
    def findDuplicate(self, nums) -> int:
        # Floyd's algorithm
        # Tortoise and Hare Algorithm
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]             # 1 step every time
            fast = nums[nums[fast]]       # 2 steps every time
        
        slow = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# testCase
nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))
nums = [3,1,3,4,2]
print(Solution().findDuplicate(nums))