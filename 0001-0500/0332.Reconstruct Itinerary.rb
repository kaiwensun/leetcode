# @param {String[][]} tickets
# @return {String[]}
def find_itinerary(tickets)
    graph = tickets.sort.reverse.group_by(&:first)
    res = []
    def dfs(node, graph, res)
        while graph.include?(node) && graph[node].any?
            dfs(graph[node].pop()[-1], graph, res)
        end
        res << node
    end
    dfs("JFK", graph, res).reverse
end
