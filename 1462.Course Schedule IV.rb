# @param {Integer} n
# @param {Integer[][]} prerequisites
# @param {Integer[][]} queries
# @return {Boolean[]}
def check_if_prerequisite(n, prerequisites, queries)
    graph = Hash.new { |h, k| h[k] = [] }
    for u, v in prerequisites
        graph[u] << v
    end
    follow_ups = Hash.new 0
    for course in 0...n
       get_follow_ups(course, graph, follow_ups) 
    end
    queries.map { |preq, follow_up| !(follow_ups[preq] & (1 << follow_up)).zero? }
end

def get_follow_ups(node, graph, follow_ups)
    if !follow_ups.include? node
        res = 0
        for neighbor in graph[node]
            res |= get_follow_ups(neighbor, graph, follow_ups) | (1 << neighbor)
        end
        follow_ups[node] = res
    end
    follow_ups[node]
end
