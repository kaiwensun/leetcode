function dividePlayers(skill: number[]): number {
    skill.sort((a, b) => a - b);
    const avg = skill[0] + skill[skill.length - 1];
    let res = 0;
    for (let i = 0; i < skill.length / 2; i++) {
        if (skill[i] + skill[skill.length - 1 - i] !== avg) return -1;
        res += skill[i] * skill[skill.length - 1 - i];
    }
    return res;
};

