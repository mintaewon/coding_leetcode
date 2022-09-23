import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = re.sub("[^a-zA-Z0-9]","",s).lower()
        s_length = len(new_s)
        for i in range((s_length//2)):
            if new_s[i] != new_s[s_length-1-i]:
                return False
        else:
            return True