from typing import List

# with sorting
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        numsSum = sum(nums)
        ansSum = 0
        while ansSum <= numsSum:
            maxValue = nums.pop()
            ans.append(maxValue)
            ansSum += maxValue
            numsSum -= maxValue
        return ans


# without sorting
class Solution2:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        ansSum = 0
        numsSum = sum(nums)
        while len(nums) > 0:
            maxNumber = max(nums)
            ans.append(maxNumber)
            nums.remove(maxNumber)
            ansSum += maxNumber
            numsSum -= maxNumber
            if ansSum > numsSum:
                return ans


# testCase
nums = [4,3,10,9,8]
print(Solution().minSubsequence(nums))
nums = [4,3,10,9,8]
print(Solution2().minSubsequence(nums))

nums = [4,4,7,6,7]
print(Solution().minSubsequence(nums))
nums = [4,4,7,6,7]
print(Solution2().minSubsequence(nums))

nums = [6]
print(Solution().minSubsequence(nums))
nums = [6]
print(Solution2().minSubsequence(nums))