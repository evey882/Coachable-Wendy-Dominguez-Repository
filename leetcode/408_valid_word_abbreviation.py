"""408. Valid Word Abbreviation"""

class Solution:
    "Solution Class"

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        This function takes a recursive approach to determine if a given abbreviation to a given word is valid.
        It is only valid if the abbreviation uses numbers that accounts for the correct number of letters in that slot that is being abbreviated on.
        When a digit is encountered it is appended and then calculated for that number of spaces, if there is a mismatched in either word past the number abbreviation it is not a valid abbreviation.
        """
        count = 0
        idx = 0

        while idx < len(abbr):
            if abbr[idx] == "0" or count >= len(word):
                return False

            number = ""
            while idx < len(abbr) and abbr[idx].isdigit():
                number += abbr[idx]
                idx += 1

            if number:
                count += int(number)
            else:
                if abbr[idx] != word[count]:
                    return False
                count += 1
                idx += 1

        return count == len(word)