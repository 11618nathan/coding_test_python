class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n_min = 100
        n_max = 0
        n_mid = 0
        for i in range(len(nums)):
            if nums[i] < n_min:
                n_mid = n_min
                n_min = nums[i]
            if nums[i] > n_max:
                n_mid = n_max
                n_max = nums[i]
            if nums[i] > n_min and nums[i] < n_max:
                n_mid = nums[i]
            if n_min < n_mid and n_max > n_mid: 
                return n_mid
        return -1