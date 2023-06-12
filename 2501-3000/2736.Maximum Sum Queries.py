from sortedcontainers import SortedList
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        if len(set(nums1)) > len(set(nums2)):
            nums1, nums2 = nums2, nums1
            for q in queries:
                q.reverse()
        queries_index = sorted([[query[0], -query[1], i] for i, query in enumerate(queries)])
        st = SortedList() #[[x, [y_i, y_i, y_i, ...]]]
        for x, ny, i in queries_index:
            if not st or st[-1][0] != x:
                st.add([x, []])
            st[-1][1].append([ny, i])
        nums = sorted([[n1 + n2, n1, n2] for n1, n2 in zip(nums1, nums2)], reverse=True)
        answers = [-1] * len(queries)
        for sm, num1, num2 in nums:
            i = st.bisect_right([num1, [[float("inf")]]])
            if i == 0:
                continue
            empty = []
            for xi in range(0, i):
                x, nys = st[xi]
                j = bisect.bisect_left(nys, [-num2, -float("inf")])
                while len(nys) > j:
                    y, qi = nys.pop()
                    answers[qi] = sm
                if not nys:
                    empty.append(xi)
            if empty:
                for xi in reversed(empty):
                    st.pop(xi)
        return answers

