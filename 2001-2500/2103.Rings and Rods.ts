function countPoints(rings: string): number {
    const counter: {[key : string]:{[key : string]: boolean}} = {};
    for (let i = 0; i < rings.length; i += 2) {
        counter[rings[i + 1]] ||= {};
        counter[rings[i + 1]][rings[i]] = true;
    }
    return Object.values(counter).reduce((acc, value) => Object.keys(value).length === 3 ? acc + 1 : acc, 0);
};

