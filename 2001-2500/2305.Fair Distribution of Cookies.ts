function distributeCookies(cookies: number[], k: number): number {
    const kids = new Array(k).fill(0);
    function dfs(c) {
        if (c === cookies.length) {
            return Math.max(...kids);
        }
        let res = Infinity;
        for (let i = 0; i < k; i++) {
            kids[i] += cookies[c];
            res = Math.min(res, dfs(c + 1));
            kids[i] -= cookies[c];
        }
        return res;
    }
    return dfs(0);
};

