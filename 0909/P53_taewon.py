# 실패 - 시간초과
from collections import deque
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        
        Q = deque(strs)
        subQ = []
        temp = []        
        answer = []
        
        while Q:
            start = Q.popleft()
            temp.append(start)
            while Q:
                a = Q.popleft()
                if sorted(start) == sorted(a):
                    temp.append(a)
                else:
                    subQ.append(a)
            answer.append(temp)
            Q = deque(subQ)
            temp = []
            subQ = []
        return answer


# dict 사용한 풀이
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s in dic:
                dic[s].append(strs[i])
            else:
                dic[s] = []
                dic[s].append(strs[i])
        return list(dic.values())