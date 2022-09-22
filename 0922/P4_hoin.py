import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", '')
        s = s.translate(str.maketrans('', '', string.punctuation))
        if len(s)==1:
            return True
        if s[::-1]==s:
            return True
        else :
            return False