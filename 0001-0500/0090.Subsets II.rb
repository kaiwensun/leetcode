# @param {Integer[]} nums
# @return {Integer[][]}
def subsets_with_dup(nums)
    counter = Hash.new 0
    nums.each { |num| counter[num] += 1 }
    res = [[]]
    for num, count in counter
        for i in 0...res.size
            for times in 1..count
                res << (res[i] + [num] * times)
            end
        end
    end
    res
end
