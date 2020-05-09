# @param {Integer} num
# @return {Boolean}
def is_perfect_square(num)
    lo, hi = 1, 46340
    while lo <= hi
        mid = lo + (hi - lo) / 2
        sqr = mid ** 2
        if sqr == num
            return true
        elsif num < sqr
            hi = mid - 1
        else
            lo = mid + 1
        end
    end
    return false
end
