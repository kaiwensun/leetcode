# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_factor(n, k)
    return -1 if k > n
    cnt = 0
    for i in 1..n
        cnt += 1 if (n % i).zero?
        return i if cnt == k
    end
    return -1
end
