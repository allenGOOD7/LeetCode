class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        all_items = items1 + items2
        
        dic = {}
        for value, weight in all_items:
            if value not in dic:
                dic[value] = weight
            else:
                dic[value] += weight
        
        res = []
        for key, value in dic.items():
            res.append([key, value])
            
        res.sort()
        
        return res