# @param {Integer[]} a
# @return {Boolean}
def split_array_same_average(a)

    return false if a.size < 2
    avg = a.sum
    (0...a.size).each { |i|  a[i] = a[i] * a.size - avg}
    left = a[0...a.size / 2]
    right = a[a.size / 2...a.size]
    lsum = left.sum
    rsum = right.sum
    left_set, lsum_cnt = all_partial_sum(left, lsum)
    right_set, rsum_cnt = all_partial_sum(right, rsum)
    if (left_set.include? 0) || (right_set.include? 0)
        return true
    end
    for l in left_set
        if l == -15
            puts "hay"
            puts right_set.include? -l
            puts l != 0 && l == lsum && lsum_cnt == 1 && -l == rsum && rsum_cnt == 1
        end
        if right_set.include? -l
            next if l == lsum && lsum_cnt == 1 && -l == rsum && rsum_cnt == 1
            return true
        end
    end
    return false
end

def all_partial_sum(arr, sum)
    count_sum = 0
    res = Set.new
    for num in arr
        for existing in res.to_a
            res << existing + num
            count_sum += 1 if existing + num == sum
        end
        res << num
        count_sum += 1 if num == sum
    end
    [res, count_sum]
end

