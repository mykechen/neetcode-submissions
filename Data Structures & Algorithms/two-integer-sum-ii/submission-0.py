class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        """
        THOUGHTS:
        - 2 pointer solution, L R on both ends
            - R pointer moves inwards if current total > target
            - L pointer moves inwards if current total < target
            - Move until total == target
        """

        left, right = 0, len(numbers) - 1

        while left < right:
            # case 1: total > target
            if numbers[left] + numbers[right] > target:
                right -= 1

            # case 2: total < target
            elif numbers[left] + numbers[right] < target:
                left += 1

            # case 3: total = target
            else:
                return [left+1, right+1]