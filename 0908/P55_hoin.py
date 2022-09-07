class Solution:
    def countSubstrings(self, s):
        if len(s)==1:
            return 1
        basic = len(s)

        for i in range(2,len(s)+1):
            sub_string=s[:i]
            start_point=0
            while len(sub_string)==i:
                sub_string=s[start_point:start_point+i]
                if len(sub_string)!=i:
                    break
                ans = check_pal(sub_string)
                start_point+=1
                basic+=ans
        return basic

def check_pal(s):
    if s[:]==s[::-1]:
        return 1
    else : 
        return 0


inputs = 'abc'
# print(check_pal(inputs))
solver = Solution()
ans = solver.countSubstrings(inputs)
print(ans)