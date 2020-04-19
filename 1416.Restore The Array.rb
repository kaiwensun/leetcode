# @param {String} s
# @param {Integer} k
# @return {Integer}
MOD = 10**9 + 7
def number_of_arrays(s, k)
    left = -1
    arr = [1] * s.size
    window_number = window_sum = 0
    for right in 0...s.size
        window_number = window_number * 10 + s[right].to_i
        while window_number > k
            window_sum -= arr[left] if s[left + 1] != "0"
            window_sum %= MOD
            left += 1
            window_number %= 10 ** (right - left)
        end
        if window_number == 0
            return 0
        end
        window_sum += arr[right - 1] if s[right] != "0"
        window_sum %= MOD
        arr[right] = window_sum
    end
    arr[-1]
end
