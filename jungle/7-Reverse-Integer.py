class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -1 * int(str(abs(x))[::-1])
        if result not in range(-2**31, 2**31):
            result = 0
        return result