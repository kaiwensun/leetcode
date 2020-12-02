import heapq, bisect
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def genMaxSubseqInc(nums, start_len, end_len):

            def compare(i, j):
                if nums[seg_tree[i]] == nums[seg_tree[j]]:
                    return min(seg_tree[i], seg_tree[j])
                elif nums[seg_tree[i]] < nums[seg_tree[j]]:
                    return seg_tree[j]
                else:
                    return seg_tree[i]

            def query(l, r):
                index = l
                l += N
                r += N + 1
                while l < r:
                    if l % 2:
                        index = compare(index + N, l)
                        l += 1
                    if r % 2:
                        index = compare(index + N, r - 1)
                        r -= 1
                    l /= 2
                    r /= 2
                return index

            def gen_next_num_index(start, end):
                if start <= end:
                    mx_index = query(start, end)
                    yield mx_index
                    for index in gen_next_num_index(mx_index + 1, end):
                        yield index
                    for index in gen_next_num_index(start, mx_index - 1):
                        yield index

            if len(nums) > end_len:
                heap = [(num, -i) for i, num in enumerate(nums)]
                nums = [item[0] for item in sorted(heapq.nlargest(end_len, heap), key=lambda item: -item[1])]
            N = len(nums)
            seg_tree = [None] * (2 * N)
            for i in xrange(len(nums)):
                seg_tree[i + N] = i

            for i in xrange(N - 1, 0, -1):
                l = i * 2
                r = i * 2 + 1
                seg_tree[i] = compare(l, r)

            index_res = []
            res = []
            if start_len == 0:
                yield res
            index_generator = gen_next_num_index(0, end_len - 1)
            for _ in xrange(end_len):
                i = next(index_generator)
                num = nums[i]
                posi = bisect.bisect(index_res, i)
                index_res.insert(posi, i)
                res.insert(posi, num)
                if len(res) >= start_len:
                    yield res

        def genMaxSubseqDec(nums, start_len, end_len):
            res = next(genMaxSubseqInc(nums, start_len, start_len))
            yield res
            start_len -= 1
            i = 0
            while i < len(res) and start_len >= end_len:
                if i != 0 and res[i - 1] < res[i]:
                    res.pop(i - 1)
                    i -= 1
                    start_len -= 1
                    yield res
                else:
                    i += 1
            while start_len >= end_len:
                start_len -= 1
                res.pop()
                yield res

        def gen_merged(nums1, nums2, i=0, j=0):
            if i == len(nums1) and j == len(nums2):
                return
            p, q = i, j
            num1 = float("-inf") if p == len(nums1) else nums1[p]
            num2 = float("-inf") if q == len(nums2) else nums2[q]
            while num1 == num2 != float("-inf"):
                num1 = float("-inf") if p == len(nums1) else nums1[p]
                num2 = float("-inf") if q == len(nums2) else nums2[q]
                p += 1
                q += 1
            if num1 >= num2:
                yield nums1[i]
                i += 1
            else:
                yield nums2[j] 
                j += 1
            for num in gen_merged(nums1, nums2, i, j):
                yield num

        start_len = k - min(len(nums2), k)
        end_len = min(len(nums1), k)
        gen1 = genMaxSubseqInc(nums1, start_len, end_len)
        gen2 = genMaxSubseqDec(nums2, k - start_len, k - end_len)
        seq1 = next(gen1, None)
        seq2 = next(gen2, None)
        res = [num for num in gen_merged(seq1, seq2)]
        while seq1 is not None and seq2 is not None:
            res = max(res, list(gen_merged(seq1, seq2)))
            seq1 = next(gen1, None)
            seq2 = next(gen2, None)

        return res

