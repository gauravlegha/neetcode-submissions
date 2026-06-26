class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        # Frequency arrays for characters 'a' through 'z'
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Initialize counts for the first window
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Check if the first window matches
        if s1_count == s2_count:
            return True

        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character to the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the oldest character from the window
            s2_count[ord(s2[i - len1]) - ord('a')] -= 1

            # Compare the frequency counts
            if s1_count == s2_count:
                return True

        return False

        