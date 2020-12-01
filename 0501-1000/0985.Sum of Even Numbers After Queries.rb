# @param {Integer[]} a
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(a, queries)
    sm = a.select(&:even?).sum
    res = []
    queries.each do |val, index|
        sm -= a[index] if a[index].even?
        a[index] += val
        sm += a[index] if a[index].even?
        res << sm
    end
    res
end

