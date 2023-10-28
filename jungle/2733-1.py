class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:        
        a = min(nums)
        b = max(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] != a and nums[i] != b:
                result.append(nums[i])
        print(result)
        if len(result) > 0:
            return result[0]
        else:
            return -1