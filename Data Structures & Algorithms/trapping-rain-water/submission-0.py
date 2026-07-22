class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        THOUGHTS:
        - 2 pointer, L and R
        - Only move L pointer if 0, or R pointer >= height[L]
        - calculate water between L and R pointer
            - min(height[L], height[R]) * (L-R) - height[i]s
            - Subtract each height[i] between each
            - L = R -> R += 1
        """ 

        l, r = 0, len(height)-1
        res = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        return res