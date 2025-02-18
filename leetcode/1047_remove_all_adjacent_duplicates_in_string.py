class Solution:
    """Solution Class"""

    def removeDuplicates(self, s: str) -> str:
        """
            In this function, the passed in string is traversed, stored in an array for easier modification. Adjacent letters are removed, this includes letter that become adjacent when another pair is removed. Leaving only characters that are different to each other, adjacently.
        """
        seen = []

        for char in s:
            if seen and seen[-1] == char:
                seen.pop()
            else:
                seen.append(char)

        return "".join(seen)