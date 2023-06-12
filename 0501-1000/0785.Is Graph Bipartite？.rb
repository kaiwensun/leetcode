# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)

    def walk(node, color=1)
        return @visited[node] == color if @visited.include? node
        @visited[node] = color
        for neighbor in @graph[node]
            return false if !walk(neighbor, -color)
        end
        true
    end

    @graph = graph
    @visited = {}
    for node in (0...graph.size)
        return false if !walk(node) if !@visited.include?(node)
    end
    true
end
