class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        """
        THOUGHTS:
        - 2 pointer problem
        - every point calculate the curr water amount
        - move the pointer that is smaller bar inwards
        """

        max_vol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            vol = (r - l) * min(heights[l], heights[r])
            max_vol = max(max_vol, vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol