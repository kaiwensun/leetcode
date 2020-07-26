# @param {Integer} n
# @param {Integer[][]} trust
# @return {Integer}
def find_judge(n, trust)
    trusters = trust.map(&:first).to_set
    if trusters.size != n - 1
        return -1
    end
    judge = ((1..n).to_set - trusters).first
    trust.select { |src, tar| tar == judge } .map(&:first).to_set.size == n - 1 ? judge : -1
end
