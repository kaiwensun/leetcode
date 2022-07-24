from collections import defaultdict

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = [None] * len(queries)
        query_dict = defaultdict(list)
        for i, query in enumerate(queries):
            query_dict[query[1]].append((i, query))
        for trim, index_query in query_dict.items():
            sorted_trimed_nums = sorted(enumerate(map(lambda s: int(s[-trim:]), nums)), key=lambda item: item[1])
            for index, query in index_query:
                res[index] = sorted_trimed_nums[query[0] - 1][0]
        return res

