import collections
class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def consume(index, target_digit, target_count, delta):
            cnt = int(target_digit == A[index])
            while cnt < target_count:
                index += delta
                cnt += int(target_digit == A[index])
            return index

        def get_internal_start_index(index, trailing_zero_cnt):
            internal_start_index = consume(index, 1, one_count, -1)
            index = consume(internal_start_index - 1, 1, 1, -1)
            if internal_start_index - index - 1 < trailing_zero_cnt:
                return None
            index += trailing_zero_cnt + 1
            return index
        def verify_equal(i, j, one_count):
            p = [0, i + 1, j]
            p = [consume(index, 1, 1, 1) for index in p]
            for _ in xrange(one_count - 1):
                new_p = [consume(index + 1, 1, 1, 1) for index in p]
                dist = [new_p[k] - p[k] for k in xrange(len(p))]
                if not (dist[0] == dist[1] == dist[2]):
                    return False
                p = new_p
            return True
            
        all_ones = collections.Counter(A)[1]
        if all_ones == 0:
            return [0, 2]
        if all_ones % 3 != 0:
            return [-1, -1]
        i, j = 0, len(A) - 1
        one_count = all_ones / 3
        j = consume(j, 1, 1, -1)
        trailing_zero_cnt = len(A) - j - 1
        j = get_internal_start_index(j, trailing_zero_cnt)
        if j is None:
            return [-1, -1]
        i = get_internal_start_index(j - trailing_zero_cnt - 1, trailing_zero_cnt)
        if i is None:
            return [-1, -1]
        i = i - 1
        if not verify_equal(i, j, one_count):
            return [-1, -1]
        return [i, j]
