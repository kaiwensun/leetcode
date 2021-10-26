function removeInvalidParentheses(s: string): string[] {
    const result = new Set<string>();
    const N = s.length;
    function getMinRemoval() {
        let debt = 0;
        let removed = 0;
        for (let c of s) {
            if (c === '(') {
                debt += 1
            } else if (c === ')') {
                if (debt == 0) {
                    removed++;
                } else {
                    debt--;
                }
            }
        }
        return debt + removed;
    }

    function dfs(i:number, debt:number, path:string[]) {
        if (debt < 0) {
            throw new Error();
        }
        if (i - path.length > minRemoval) {
            return;
        }
        if (i === N && debt === 0) {
            result.add(path.join(''));
            return;
        }
        if (debt > N - i) {
            return;
        }
        if (s[i] === '(') {
            path.push('(');
            dfs(i + 1, debt + 1, path);
            path.pop();
            dfs(i + 1, debt, path);
        } else if (s[i] === ')') {
            if (debt > 0) {
                path.push(')');
                dfs(i + 1, debt - 1, path);
                path.pop();
            }
            dfs(i + 1, debt, path)
        } else {
            path.push(s[i]);
            dfs(i + 1, debt, path);
            path.pop()
        }
    }
    const minRemoval = getMinRemoval();
    dfs(0, 0, []);
    return [...result];
};

