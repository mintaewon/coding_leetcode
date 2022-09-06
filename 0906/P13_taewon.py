from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        # 바로 이전 괄호를 확인하기 위한 함수
        def func(t):
            if t == ")":
                return "("
            elif t == "]":
                return "["
            elif t == "}":
                return "{"
        
        # 괄호가 홀수개면 False
        if len(s)%2 == 1:
            return False
        # 닫는괄호로 시작하면 False
        if (s[0]==")") or (s[0]=="]") or (s[0]=="}"):
            return False
        
        stack = deque()
        for i in s:
            # 여는 괄호 stack에 추가
            if (i=="(") or (i=="{") or (i=="["):
                stack.append(i)
            else:
                # 닫는 괄호 나오면 확인
                if len(stack)!=0 and stack[-1] == func(i):
                    stack.pop()
                else:
                    return False
                
        # 반복문 종료 후 stack에 괄호가 남아있으면 False
        if len(stack) == 0:
            return True
        else:
            return False
        return True