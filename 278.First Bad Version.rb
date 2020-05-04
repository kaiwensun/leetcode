# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    left, right = 1, n + 1
    while left != right
        mid = (left + right) / 2
        is_bad = is_bad_version(mid)
        if is_bad
            right = mid
        else
            left = mid + 1
        end
    end
    left
end
