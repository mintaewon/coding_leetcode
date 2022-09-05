class Solution:
    def isValid(self, s):
        st = []
        if s[0] in [')','}',']']:
            return False
        for i in s: 
            try : 
                if i=='(' or i=='{' or i=='[':
                    st.append(i)

                elif i==')':
                    if st[-1]=='(':
                        st.pop(-1)
                    else :
                        return False        
                elif i=='}':
                    if st[-1]=='{':
                        st.pop(-1)
                    else :
                        return False
                elif i==']':
                    if st[-1]=='[':
                        st.pop(-1)
                    else :
                        return False
            except IndexError:
                return False
            
        if len(st)==0:
            return True
        else :
            return False


solver = Solution()
s ="(){}}{"
print(solver.isValid(s))
        