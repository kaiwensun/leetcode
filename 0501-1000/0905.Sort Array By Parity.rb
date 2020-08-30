# @param {Integer[]} a
# @return {Integer[]}
def sort_array_by_parity(a)
    i, j = 0, a.size - 1
    while i < j
        if a[i].even?
            i += 1
        else
            a[i], a[j] = a[j], a[i]
            j -= 1
        end
    end
    a
end
