# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    graph = Hash.new { |h, k| h[k] = [] }
    cnt = Hash.new 0
    seen = Set.new
    for fst, snd in prerequisites
        graph[fst] << snd
        cnt[snd] += 1
        cnt[fst] += 0
    end
    for course in cnt.keys
        return false if not dfs(course, graph, seen) if cnt[course].zero?
    end
    seen.size == cnt.size
end

def dfs(course, graph, seen, path=Set.new)
    return false if path.add?(course).nil?
    if not seen.add?(course).nil?
        for neighbor in graph[course]
            return false if !dfs(neighbor, graph, seen, path)
        end
    end
    path.delete course
    true
end
