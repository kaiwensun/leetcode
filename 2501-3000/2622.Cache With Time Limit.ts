class TimeLimitedCache {
    private map;
    constructor() {
        this.map = {};
    }

    set(key: number, value: number, duration: number): boolean {
        const now = new Date().getMilliseconds();
        let res = !!this.map[key];
        this.map[key] = [value, now, duration];
        setTimeout(() => {
            const record = this.map[key]
            if (record) {
                if (record[0] === value && record[1] === now && record[2] === duration) {
                    delete this.map[key];
                }
            }
        }, duration);
        return res;
    }

    get(key: number): number {
        const res = this.map[key];
        return res === undefined ? -1 : res[0];
    }

	count(): number {
        return Object.keys(this.map).length;
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */

