# @param {Integer[][]} a
# @return {Integer[][]}
def transpose(a)
    res = []
    a.each_with_index do |row, i|
        row.each_with_index do |col, j|
            res << [] if i == 0
            res[j] << a[i][j]
        end
    end
    res
end
