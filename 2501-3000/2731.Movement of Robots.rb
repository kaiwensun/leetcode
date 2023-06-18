# @param {Integer[]} nums
# @param {String} s
# @param {Integer} d
# @return {Integer}

MOD = 10e8.to_i + 7
def sum_distance(nums, s, d)
    positions = nums.zip(s.split("")).map{ |posi| posi[0] + (posi[1] == 'R' ? d : -d) }.sort
    res = 0
    times = 1
    n = positions.length.freeze
    for i in 1...n do
        res += (positions[i] - positions[i - 1]) * i * (n - i)
        res %= MOD
        times += 1
    end
    return res
end

