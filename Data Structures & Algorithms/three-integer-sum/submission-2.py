class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        THOUGHTS:
        - Sort the array, and use 2 pointers on each side with a temp pointer looping through
        - L, R, and a temp pointer moving between them adding the total up to see if == 0
        - if total > 0, move R inwards
        - if total < 0, move L inwards
        """

        #       L   i        R
        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l], num, nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res