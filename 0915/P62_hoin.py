class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        data = dict(dic)
        dict_data = collections.OrderedDict(sorted(data.items(),reverse=True, key=operator.itemgetter(1)))
        return list(dict_data)[:k]
        
        