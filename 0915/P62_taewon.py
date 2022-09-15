from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for a,_ in Counter(nums).most_common(k):
            answer.append(a)
        return answer