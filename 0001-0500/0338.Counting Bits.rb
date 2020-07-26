# @param {Integer} num
# @return {Integer[]}
def count_bits(num)
    res = Array.new(num + 1)
    (0..num).each do |i|
        if i <= 1
            res[i] = i
        else
            res[i] = res[i >> 1] + (i.odd? ? 1 : 0)
        end
    end
    res
end
