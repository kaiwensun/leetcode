function countSubarrays(nums: number[], k: number): number {
    function divideAndConquer(start: number, end: number) {
        if (start === end) {
            return 0;
        }
        if (start + 1 === end) {
            return nums[start] < k ? 1 : 0;
        }
        const mid = (start + end) >> 1;
        let res = divideAndConquer(start, mid) + divideAndConquer(mid, end);
        let sum = 0, left = mid - 1;
        while (left >= start && (sum + nums[left]) * (mid - left) < k) {
            sum += nums[left--];
        }
        for (let right = mid; right < end; right++) {
            sum += nums[right];
            while (sum * (right - left) >= k) {
                sum -= nums[++left];
            }
            if (left >= mid - 1) {
                break;
            }
            res += mid - left - 1;
        }
        return res;
    }
    return divideAndConquer(0, nums.length);
};

