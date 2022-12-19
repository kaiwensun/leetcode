class Allocator {
    private memory;
    private midMap;
    constructor(n: number) {
        this.memory = new Array(n);
        this.midMap = {};
    }

    allocate(size: number, mID: number): number {
        for (let start = 0; start < this.memory.length - size + 1; start++) {
            let i: number;
            for (i = start; i < start + size; i++) {
                if (this.memory[i]) break;
            }
            if (i === start + size) {
                for (i = start; i < start + size; i++) {
                    this.memory[i] = mID;
                }
                this.midMap[mID] ||= [];
                this.midMap[mID].push(start);
                return start;
            } else {
                start = i;
            }
        }
        return -1;
    }

    free(mID: number): number {
        let res = 0;
        for (let start of (this.midMap[mID] || [])) {
            for (let i = start; i < this.memory.length && this.memory[i] === mID; i++) {
                this.memory[i] = undefined;
                res++;
            }
        }
        this.midMap[mID] = [];
        return res;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = new Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.free(mID)
 */

