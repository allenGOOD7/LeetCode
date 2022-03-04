from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for index, num in enumerate(nums):
            if target - num not in dic:
                dic[num] = index
            else:
                return [dic[target - num], index]

print(Solution().twoSum(nums = [2,7,11,15], target = 9))