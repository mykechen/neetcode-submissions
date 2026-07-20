class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        THOUGHTS:
        - Make lookup O(1) so convert nums into a set
        - Want to find the starting points meaning only searching when current num - 1 doesnt exist in the set
        - Once found starting point, keep looping and updating length until nums + length no longer in set
        - return the max between cur length and longest
        """

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest

        

    