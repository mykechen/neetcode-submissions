class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        THOUGHTS:
        - Dynamic sliding window
        - Keep expanding the window until k = 0 and the next char is different from the starting char
            - if same char, keep expanding
            - if diff char, k -= 1
        - calculate max_length every run
        - resize window, and subtract the left char from the window, until it hits the new character
        """

        count = defaultdict(int)
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
