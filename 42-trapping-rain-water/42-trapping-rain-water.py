class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack = []
        
        for i in range(n):
            l = len(stack)
            if l == 0 or height[i] < height[stack[l - 1]]:
                stack.append(i)
            else:
                while(l > 0 and height[stack[l - 1]] <= height[i]):
                    ht = height[stack.pop()]
                    l = l - 1
                    ans = ans + (0 if l == 0 else (min(height[i],height[stack[l - 1]]) - ht) * (i - stack[l - 1] - 1))
                stack.append(i)
        return ans
        
     