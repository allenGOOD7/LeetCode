class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def search(x):
            l, r = 0, len(nums) - 1
            while r >= l:
                mid = (l + r) // 2
                if nums[mid] >= x:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        start = search(target)
        end = search(target + 1) - 1

        if start > end:
            return [-1, -1]
        return [start, end]