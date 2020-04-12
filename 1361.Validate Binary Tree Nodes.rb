# @param {Integer} n
# @param {Integer[]} left_child
# @param {Integer[]} right_child
# @return {Boolean}
def validate_binary_tree_nodes(n, left_child, right_child)
    def dfs(node)
        if node == -1
            true
        elsif @visited.include? node
            false
        else
            @visited << node
            dfs(@left_child[node]) and dfs(@right_child[node])
        end
    end
    sources = ((0...n).to_set - left_child.to_set - right_child.to_set)
    @left_child, @right_child, @visited = left_child, right_child, Set.new
    sources.one? and dfs(sources.first) and @visited.size == n
end
