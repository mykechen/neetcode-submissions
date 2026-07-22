class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        THOUGHTS:
        - dynamic sliding window
        - compare the next char to the first char, if they are the same, remove the first char and add the car
        - if diff, add the char to the window, increasing the size, repeat till the end
        - return the window size at the end
        """

        left = 0
        res = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            res = max(res, right - left + 1)

        return res