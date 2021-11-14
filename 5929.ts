function friendRequests(n: number, restrictions: number[][], requests: number[][]): boolean[] {
    const data = Array(n);
    for (let i = 0; i < n; i++) {
        data[i] = i;
    }

    function find(x: number) {
        if (data[x] !== x) {
            data[x] = find(data[x]);
        }
        return data[x];
    }

    function union([x, y]: number[]) {
        let rx = find(x);
        let ry = find(y);
        if (rx !== ry) {
            for (let i = 0; i < restrictions.length; i++) {
                let r1 = find(restrictions[i][0]);
                let r2 = find(restrictions[i][1]);
                if ((rx === r1 && ry === r2) || (ry === r1 && rx === r2)) {
                    return false;
                }
            }
            data[rx] = ry;
        }
        return true;
    }

    return requests.map(union);
};

