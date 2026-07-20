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

        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            
            i = left + 1
            right = len(nums) - 1
            
            while i < right:
                target = nums[left] + nums[i] + nums[right]
                if target == 0:
                    res.append([nums[left], nums[i], nums[right]])
                    while i < right and nums[i] == nums[i + 1]:
                        i += 1
                    while i < right and nums[right] == nums[right - 1]:
                        right -= 1
                    i += 1
                    right -= 1
                elif target < 0:
                    i += 1
                else:
                    right -= 1

        return res