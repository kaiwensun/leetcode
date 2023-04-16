# @param {Integer[]} nums
# @param {Integer[]} divisors
# @return {Integer}
def max_div_score(nums, divisors)
    nums.sort! { |a, b| b - a }
    res = [0, -divisors[0]]
    for divisor in divisors
        cnt = 0
        for num in nums
            if num < divisor
                break
            end
            if num % divisor == 0
                cnt += 1
            end
        end
        res = [res, [cnt, -divisor]].max
    end
    -res[1]
end

