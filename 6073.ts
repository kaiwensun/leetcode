function longestPath(parent: number[], s: string): number {
    const N = s.length;
    const roots = new Set([0]);
    const graph = {};
    for (let i = 1; i < N; i++) {
        const p = parent[i];
        if (s[i] === s[p]) {
            roots.add(i);
        } else {
            graph[p] ||= [];
            graph[p].push(i);
        }
    }

    function dfs(node) {
        // return [max path to node, max path in subtree]
        let maxPath = 0;
        const pathsToNode = [0, 0];
        for (const child of graph[node] || []) {
            let [subtreeMaxToChild, subtreeMax] = dfs(child);
            if (subtreeMaxToChild > pathsToNode[1]) {
                pathsToNode[1] = subtreeMaxToChild;
                if (pathsToNode[0] < pathsToNode[1]) {
                    const tmp = pathsToNode[1]; pathsToNode[1] = pathsToNode[0]; pathsToNode[0] = tmp;
                }
            }
            maxPath = Math.max(maxPath, subtreeMax);
        }
        maxPath = Math.max(maxPath, pathsToNode[0] + pathsToNode[1] + 1);
        return [pathsToNode[0] + 1, maxPath];
    }

    return [...roots].map(node => dfs(node)[1]).reduce((a, b) => Math.max(a, b), 0);
};


