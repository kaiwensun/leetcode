# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def min_sum_of_lengths(arr, target)
    # seen = {}
    l = sum = 0
    window_sizes = Array.new(arr.size, [Float::INFINITY] * 2) # [last_window_size, prev_min_window_size]
    for r in 0...arr.size
        sum += arr[r]
        until sum <= target
            sum -= arr[l]
            l += 1
        end
        if sum == target
            window_sizes[r] = [r - l + 1, [window_sizes[r - 1].last, r - l + 1].min]
        else
            window_sizes[r] = [Float::INFINITY, window_sizes[r - 1].last]
        end
    end
    res = window_sizes.each_with_index.map { |size, index| size.first + (index - size.first < 0 ? Float::INFINITY : window_sizes[index - size.first].last) } .min
    res.infinite? ? -1 : res
end
