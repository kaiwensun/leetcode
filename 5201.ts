function wateringPlants(plants: number[], capacity: number): number {
    let water = capacity, steps = plants.length;
    for (let i = 0; i < plants.length; i++) {
        if (water < plants[i]) {
            steps += i * 2;
            water = capacity;
        }
        water -= plants[i];
    }
    return steps;
};

