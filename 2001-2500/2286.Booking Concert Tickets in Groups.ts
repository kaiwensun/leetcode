class BookMyShow {
    private smallestST: number[];
    private sumST: number[];
    private m: number;
    private n: number;
    constructor(n: number, m: number) {
        this.m = m;
        this.n = n;
        this.smallestST = new Array(n * 2).fill(0);
        this.sumST = new Array(n * 2).fill(0);
    }

    gather(k: number, maxRow: number): number[] {
        const i = this.binarySearch(0, maxRow + 1, mid => {
            const smallest = this.searchST(0, mid + 1, this.smallestST, Math.min, Infinity);
            return smallest + k > this.m;
        });
        if (i <= maxRow) {
            const res = [i, this.smallestST[this.n + i]];
            this.updateSmallestST(i, k);
            this.updateSumST(i, k);
            return res;
        } else {
            return [];
        }
    }

    scatter(k: number, maxRow: number): boolean {
        const sm = this.searchST(0, maxRow + 1, this.sumST, (a, b) => a + b, 0);
        if (k <= (1 + maxRow) * this.m - sm) {
            let i = 0;
            while (k) {
                const newSit = Math.min(k, this.m - this.smallestST[this.n + i]);
                this.updateSmallestST(i, newSit);
                this.updateSumST(i, newSit);
                k -= newSit;
                i++;
            }
            return true;
        } else {
            return false;
        }
    }

    private updateST(i, addValue, st, aggregator) {
        i += this.n;
        st[i] += addValue;
        while (i) {
            i >>= 1;
            st[i] = aggregator(st[i * 2], st[i * 2 + 1]);
        }
    }

    private updateSmallestST(i, addValue) {
        this.updateST(i, addValue, this.smallestST, Math.min);
    }

    private updateSumST(i, addValue) {
        this.updateST(i, addValue, this.sumST, (a, b) => a + b);
    }

    private searchST(start, end, st, calculator, initVal) {
        start += this.n;
        end += this.n;
        let res = initVal;
        while (start < end) {
            if (start & 1) {
                res = calculator(res, st[start]);
                start++;
            }
            if (end & 1) {
                end--;
                res = calculator(res, st[end]);
            }
            start >>= 1;
            end >>= 1;
        }
        return res;
    }

    private binarySearch(start: number, end: number, test: (num:number) => boolean): number {
        while (start < end) {
            const mid = (start + end) >> 1;
            if (test(mid)) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */

