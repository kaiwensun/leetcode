# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
    stones.sort!
    while stones.size > 1
        x = stones.pop
        y = stones.pop
        if x > y
            index = stones.bsearch_index { |n| n >= x - y }
            stones.insert(index.nil? ? stones.size : index, x - y)
        end
    end
    stones.size == 1 ? stones[0] : 0
end
