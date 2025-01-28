"""680. Valid Palindrome II"""

class Solution:
    """Solution Class"""

    def checkPalindrome(self, s: str, low: int, high: int, flag: bool) -> bool:
        """
            This function is used as a helper to recursively determine if by removing one letter we are able to validate for a palindrome.
            A flag is used to determine that a letter has been removed and then the helper function is called on the remaining letters, if the two pointer comparison's reach each other, then it is a valid palindrome, 
            if they can't and the flag is triggered then it is not.
        """
        while low < high:
            if s[low] != s[high]:
                if not flag:
                    flag = True
                    return self.checkPalindrome(s, low + 1, high, flag) or self.checkPalindrome(s, low, high - 1, flag)
                else:
                    return False

            low += 1
            high -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        removed_char = False
        return self.checkPalindrome(s, low, high, removed_char)