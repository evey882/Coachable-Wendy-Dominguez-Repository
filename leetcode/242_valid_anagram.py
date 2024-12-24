"""242. Valid Anagram"""

class Solution:
    """Solution Class"""

    def counter(self, s: str):
        """
            This function helps return the character map to the main function.
            It is refactored so it is easier to read.
        """
        counter = {}

        for char in s:
            if char not in counter:
                counter[char] = 0

            counter[char] += 1

        return counter

    def isAnagram(self, s: str, t: str) -> bool:
        """
            This function determines if two strings are anagrams of each other.
            With anagrams the order doesn't matter and so this solution gets the char
            map of each string, as they should have the same amount of each char. It
            does this by calling a helper function that goes through each one in O(n)
            time where n is the length of the longest string.
        """
        counter_s = self.counter(s)
        counter_t = self.counter(t)

        return counter_s == counter_t