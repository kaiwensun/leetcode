# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
    lo, hi = 0, citations.size
    while lo < hi
        mid = (lo + hi) / 2
        if citations[mid] < citations.size - mid
            lo = mid + 1
        else
            hi = mid
        end
    end
    citations.size - hi
end
