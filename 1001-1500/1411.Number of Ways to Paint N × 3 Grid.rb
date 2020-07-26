# @param {Integer} n
# @return {Integer}
MOD = 10 ** 9 + 7
$pattern121 = [1]
$pattern123 = [1]
def num_of_ways(n)
    while $pattern123.size < n
        new121 = ($pattern121[-1] * 3 + $pattern123[-1] * 2) % MOD
        new123 = ($pattern121[-1] * 2 + $pattern123[-1] * 2) % MOD
        $pattern121 << new121
        $pattern123 << new123
    end
    return ($pattern121[n - 1] * 6 + $pattern123[n - 1] * 6) % MOD
end
