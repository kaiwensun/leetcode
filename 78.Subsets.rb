# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    res = [[]]
    for num in nums
        for i in 0...res.size
            res << (res[i].clone << num)
        end
    end
    res
end
