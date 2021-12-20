function findRadius(houses: number[], heaters: number[]): number {
    let i = 0, res = 0;
    console.log(houses.sort((a, b) => a - b));
    console.log(heaters.sort((a, b) => a - b));
    
    heaters.push(Infinity);
    heaters.unshift(-Infinity);
    for (const house of houses) {
        while (!(heaters[i] <= house && house <= heaters[i + 1])) {
            i++;
        }
        res = Math.max(res, Math.min(house - heaters[i], heaters[i + 1] - house));
    }
    return res;
};


