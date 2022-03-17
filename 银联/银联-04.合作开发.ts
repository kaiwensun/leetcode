function coopDevelop(skills: number[][]): number {
    const MOD = 1e9 + 7;
    const count = {};
    let nonCollaborative = 0;
    skills.map(skill => skill.sort()).map(skill => skill.toString()).forEach(skill => {
        count[skill] ||= 0;
        count[skill]++;
    });
    function subsets(skill) {
        const res = [];
        (function dfs(i, path) {
            if (i === skill.length) {
                if (path.length && skill.length - path.length) {
                    res.push(path.slice());
                }
            } else {
                dfs(i + 1, path);
                path.push(skill[i]);
                dfs(i + 1, path);
                path.pop();
            }
        })(0, []);
        return res;
    }
    for (const skill of Object.keys(count)) {
        let partners = count[skill] - 1;
        for (const subset of subsets(skill.split(","))) {
            partners += (count[subset.toString()] || 0) * 2;
        }
        nonCollaborative += count[skill] * partners;
    }
    return (skills.length * (skills.length - 1) - nonCollaborative) / 2 % MOD;
};

