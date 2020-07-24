class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        return allPathsSourceTarget(graph, 0);
    }
    
    private List<List<Integer>> allPathsSourceTarget(int[][] graph, int node) {
        List<List<Integer>> res = new LinkedList<>();
        if (node == graph.length - 1) {
            List<Integer> path = new LinkedList<>();
            path.add(node);
            res.add(path);
        } else {
            for (int next : graph[node]) {
                List<List<Integer>> paths = allPathsSourceTarget(graph, next);
                if (paths.size() != 0) {
                    res.addAll(paths);
                }
            }
            for (List<Integer> path : res) {
                path.add(0, node);
            }
        }
        return res;
    }
}
