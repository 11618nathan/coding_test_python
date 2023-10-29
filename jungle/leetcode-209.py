class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        l = 0
        sub_sum = 0
        for r, n in enumerate(nums):
            sub_sum += n # 해당 원소를 더해줌
            while sub_sum >= target:
                result = min(result, r - l + 1)
                sub_sum -= nums[l]
                l += 1
        return result % (len(nums) + 1)