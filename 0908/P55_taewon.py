class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for start in range(len(s)):
            end = start+1
            while end <= len(s):
                temp = s[start:end]
                if temp == temp[::-1]:
                    answer += 1
                end += 1
        return answer