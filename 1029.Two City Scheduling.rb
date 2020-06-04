# @param {Integer[][]} costs
# @return {Integer}
def two_city_sched_cost(costs)
    costs.sort_by { |cost| cost[0] - cost[1] }
        .each_with_index
        .map { |cost, index| index < costs.size / 2 ? cost[0] : cost[1] }
        .sum
end
