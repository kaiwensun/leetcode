# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def hamming_distance(x, y)
    dist, mask = 0, 1
    while x != y
        dist += 1 if x & mask != y & mask
        x &= ~mask
        y &= ~mask
        mask <<= 1
    end
    dist
end
