class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        cout = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                cout += distance * waters
            stack.append(i)
        return cout