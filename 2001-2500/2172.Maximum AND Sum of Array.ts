function maximumANDSum(nums: number[], numSlots: number): number {
    const DP = [];
    function dfs(i, slotSetting) {
        if (i === nums.length) {
            return 0;
        }
        if (i == DP.length) {
            DP.push({});
        }
        if (DP[i].hasOwnProperty(slotSetting)) {
            return DP[i][slotSetting];
        }
        let slotIter = slotSetting;
        let slotId = 0;
        let res = -Infinity;
        while (slotIter !== 0) {
            const space = slotIter & 3;
            if (space !== 0) {
                res = Math.max(res, ((slotId + 1) & nums[i]) + dfs (i + 1, slotSetting - (1 << (slotId * 2))));
            }
            slotId++;
            slotIter >>= 2;
        }
        DP[i][slotSetting] = res;
        return res;
    }
    let slotSettings = 0;
    for (let i = 0; i < numSlots; i++) {
        slotSettings <<= 2;
        slotSettings += 2;
    }
    return dfs(0, slotSettings);
};

