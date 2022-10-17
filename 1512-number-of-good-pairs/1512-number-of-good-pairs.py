class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = [index]
            else:
                dic[num].append(index)
        
        res = 0
        for value in dic.values():
            if len(value) > 1:
                temp = (len(value) - 1) * len(value) / 2
                res += temp
        return int(res)