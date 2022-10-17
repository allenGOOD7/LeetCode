class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        res = 0
        for value in dic.values():
            if value > 1:
                temp = (value - 1) * value / 2
                res += temp
        return int(res)