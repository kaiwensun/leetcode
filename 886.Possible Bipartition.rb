# @param {Integer} n
# @param {Integer[][]} dislikes
# @return {Boolean}
def possible_bipartition(n, dislikes)
    graph = Hash.new { |h, k| h[k] = [] }
    for u, v in dislikes
        graph[u] << v
        graph[v] << u
    end
    def dfs(u, color, colors, graph)
        if colors.include? u
            return colors[u] == color
        else
            colors[u] = color
            for v in graph[u]
                return false if !dfs(v, -color, colors, graph)
            end
            true
        end
    end
    colors = {}
    for u in (1..n)
        if !colors.include? u
            return false if !dfs(u, 1, colors, graph)
        end
    end
    true
end
