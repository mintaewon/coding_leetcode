class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        k=32-len(s)
        add = '0'*k 
        s = add + s
        cnt=0
        num=0
        for i in range(len(s)) :
            num+=int(s[i])*(2**cnt)
            cnt+=1
        return num