# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def max_uncrossed_lines(a, b)
    @dp, @a, @b = Hash.new(0), a, b
    def search(i, j)
        return 0 if i < 0 || j < 0
        if !@dp.include? [i, j]
            @dp[[i, j]] = search(i - 1, j - 1) + 1 if @a[i] == @b[j]
            @dp[[i, j]] = [@dp[[i, j]], search(i - 1, j), search(i, j - 1)].max
        end
        @dp[[i, j]]
    end
    search(a.size - 1, b.size - 1)
end
