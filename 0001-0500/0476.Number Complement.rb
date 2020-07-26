# @param {Integer} num
# @return {Integer}
def find_complement(num)
    mask = [1, 2, 4, 8, 16].reduce(num) { | mask, shift | mask | mask >> shift }  
    ~num & mask
end
