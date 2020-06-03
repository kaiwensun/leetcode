# @param {Integer[][]} costs
# @return {Integer}
def two_city_sched_cost(costs)
    indexes = costs.each_with_index
        .map { |cost, i| [cost[0] - cost[1], i] }
        .sort
        .map(&:last)
        .each_with_index
        .map { |index, new_index| (new_index < costs.size / 2) ? costs[index][0] : costs[index][1] }
        .sum
end
