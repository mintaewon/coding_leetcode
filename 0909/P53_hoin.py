from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs):
        ana_dict = defaultdict(list)
        for s in strs:
            # ana_dict[tuple(sorted(Counter(s)))].append(s)
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ana_dict[tuple(count)].append(s)
        return ana_dict.values()
solver=Solution()
strs = ["ddddddddddg","dgggggggggg"]
print(solver.groupAnagrams(strs))
