class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        new_ls = sorted(intervals, key=lambda x: (x[0], x[1]))
        answer = 0
        check = new_ls[0][1]
        for start, end in new_ls[1:]:
            if start < check:
                answer += 1
                check = min(check, end)
            else:
                check = end
        return answer