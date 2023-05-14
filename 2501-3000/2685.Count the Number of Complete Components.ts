function countCompleteComponents(n: number, edges: number[][]): number {
    const data = new Array(n);
    for (let i = 0; i < n; i++) {
        data[i] = i;
    }
    function find(x) {
        if (data[x] !== x) {
            data[x] = find(data[x]);
        }
        return data[x];
    }
    function union(x, y) {
        const rx = find(x);
        const ry = find(y);
        if (rx !== ry) {
            data[rx] = ry;
        }
    }
    
    edges.forEach(edge => {
        union(edge[0], edge[1]);
    });

    const groups: {[key: number]: number[]} = {};
    data.forEach((_, i) => {
        const root = find(i);
        groups[root] ||= [];
        groups[root].push(i);
    });
    
    const counts = {};
    edges.forEach(edge => {
        edge.forEach(node => {
            counts[node] ||= 1; counts[node]++;
        });
    });
    
    let res = Object.keys(groups).length;
    
    Object.values(groups).forEach(group => {
        const size = group.length;
        for (const member of group) {
            if (counts[member] !== undefined && counts[member] !== size) {
                res--;
                break;
            }
        }
    });
    return res;
};

