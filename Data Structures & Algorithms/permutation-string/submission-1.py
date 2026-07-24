class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        THOUGHTS:
        - fixed sliding window of len of s1
        - store the counts of s1 in a fixed array and just compare the position of them
        """

        # check len(s1) > len(s2)
        if len(s1) > len(s2):
            return False

        # use a defaultdict(int) to store the counts of each character
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        # get first len(s1) and check with s2 if they are same
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        # check if they are same
        if s1_count == s2_count:
            return True

        # fixed sliding window across s2
        left = 0
        for right in range(len(s1), len(s2)):
            # add new character
            # delete oldest character
            s2_count[s2[right]] += 1
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            # check if they are permutations
            if s1_count == s2_count:
                return True

        return False
