class Solution {
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        Map<Integer, List<Integer>> rowGraph = buildGraph(rowConditions, k);
        Map<Integer, List<Integer>> colGraph = buildGraph(colConditions, k);
        List<Integer> rowOrder = topologicalSort(rowGraph);
        List<Integer> colOrder = topologicalSort(colGraph);
        if (rowOrder == null || colOrder == null) {
            return new int[0][0];
        }
        int[][] positions = findPositions(rowOrder, colOrder);
        int[][] result = new int[k][k];
        for (int i = 0; i < k; i++) {
            result[positions[i][0]][positions[i][1]] = i + 1;
        }
        return result;
    }

    private int[][] findPositions(List<Integer> rowOrder, List<Integer> colOrder) {
        final int k = rowOrder.size() - 1;
        int[][] result = new int[k][2];
        for (int i = 0; i <= k; i++) {
            if (rowOrder.get(i) != 0) result[rowOrder.get(i) - 1][0] = k - 1 - i;
        }
        for (int i = 0; i <= k; i++) {
            if (colOrder.get(i) != 0)  result[colOrder.get(i) - 1][1] = k - 1 - i;
        }
        return result;
    }

    private Map<Integer, List<Integer>> buildGraph(int[][] conditions, int k) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] condition : conditions) {
            graph.putIfAbsent(condition[0], new LinkedList<Integer>());
            graph.get(condition[0]).add(condition[1]);
        }
        graph.put(0, IntStream.range(1, k + 1).boxed().collect(Collectors.toList()));
        return graph;
    }

    private List<Integer> topologicalSort(Map<Integer, List<Integer>> graph) {
        List<Integer> result = new ArrayList<>(graph.get(0).size());
        Set<Integer> visiting = new HashSet<>();
        Set<Integer> visited = new HashSet<>();
        if (dfs(graph, 0, visiting, visited, result)) {
            return result;
        }
        return null;
    }

    private boolean dfs(Map<Integer, List<Integer>> graph, Integer cur, Set<Integer> visiting, Set<Integer> visited, List<Integer> collector) {
        if (visited.contains(cur)) {
            return true;
        }
        if (visiting.contains(cur)) {
            return false;
        }
        visiting.add(cur);
        for (Integer nxt : graph.getOrDefault(cur, Collections.emptyList())) {
            if (!dfs(graph, nxt, visiting, visited, collector)) {
                return false;
            }
        }
        collector.add(cur);
        visited.add(cur);
        return true;
    }
}

