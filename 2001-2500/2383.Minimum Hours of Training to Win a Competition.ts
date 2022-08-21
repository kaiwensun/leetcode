function minNumberOfHours(initialEnergy: number, initialExperience: number, energy: number[], experience: number[]): number {
    let res = 0;
    for (let i = 0; i < energy.length; i++) {
        res += Math.max(energy[i] + 1 - initialEnergy, 0);
        res += Math.max(experience[i] + 1 - initialExperience, 0);
        initialEnergy = Math.max(initialEnergy, energy[i] + 1);
        initialExperience = Math.max(initialExperience, experience[i] + 1);
        initialEnergy -= energy[i];
        initialExperience += experience[i];
    }
    return res;
};

