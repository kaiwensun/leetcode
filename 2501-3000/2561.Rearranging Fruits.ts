/*
 要么用最小的min当工具人，连续换两次，以交换其他两个数；
 要么用array里i指向的最小值换array后半部分较大的。
 basket1和basket2中需要被换的数，可以一股脑放进array里，无需考虑是从哪个basket换到哪个basket。
*/
function minCost(basket1: number[], basket2: number[]): number {
    const N = basket1.length;
    const counter: {[key: number] : number} = {};
    for (let i = 0; i < N; i++) {
        counter[basket1[i]] ||= 0;
        counter[basket1[i]]++;
        counter[basket2[i]] ||= 0;
        counter[basket2[i]]--;
    }
    const min = Math.min(...Object.keys(counter).map(num => parseInt(num)));
    const array: number[] = [];
    if (Object.values(counter).some(value => value % 2)) {
        return -1;
    }
    Object.entries(counter).sort((a, b) => parseInt(a[0]) - parseInt(b[0])).forEach(([key, value]) => {
        const num = parseInt(key);
        for (let i = 0; i < Math.abs(value) / 2; i++) {
            array.push(num);
        }
    });
    const half = array.slice(0, array.length / 2);
    return half.reduce((acc, num) => acc + Math.min(min * 2, num), 0);
};

