class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        THOUGHTS:
        - Store each num in nums into a set
        - Want to find the starting points, so only check if nums-1 does not exist in set
            - if doesnt exist, possible starting point
        """

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

    