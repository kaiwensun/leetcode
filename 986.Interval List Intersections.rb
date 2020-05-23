# @param {Integer[][]} a
# @param {Integer[][]} b
# @return {Integer[][]}
def interval_intersection(a, b)
    i = j = 0
    res = []
    while i < a.size && j < b.size
        if a[i][0] > b[j][0]
            a, b = b, a
            i, j = j, i
        end
        cur = [[a[i][0], b[j][0]].max, [a[i][1], b[j][1]].min]
        if cur[0] > cur[1]
            i += 1
            next
        end
        res << cur
        a[i][0] = cur[1] + 1
        b[j][0] = cur[1] + 1
        i += 1 if a[i][0] > a[i][1]
        j += 1 if b[j][0] > b[j][1]
    end
    res
end
