class Solution {
    
    int res = 0;

    public int treeDiameter(int[][] edges) {
        this.res = 0;
        Map<Integer, List<Integer>> graph = makeGraph(edges);
        dfs(graph, 0, -1);
        return this.res;
    }
    
    private Map<Integer, List<Integer>> makeGraph(int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.putIfAbsent(edge[0], new LinkedList<Integer>());
            graph.putIfAbsent(edge[1], new LinkedList<Integer>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        return graph;
    }
    
    private int dfs(Map<Integer, List<Integer>> graph, int node, int prev) {
        int[] bigs = new int[] {0, 0};
        for (int neighbor : graph.get(node)) {
            if (neighbor != prev) {
                bigs = big2(bigs, dfs(graph, neighbor, node));
            }
        }
        this.res = Math.max(res, bigs[0] + bigs[1]);
        return bigs[0] + 1;
    }
    
    private int[] big2(int[] curBigs, int candidate) {
        for (int i = 0; i < 2; i++) {
            if (candidate > curBigs[i]) {
                int tmp = candidate; candidate = curBigs[i]; curBigs[i] = tmp;
            }
        }
        return curBigs;
    }
}
