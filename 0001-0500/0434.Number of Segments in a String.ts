function countSegments(s: string): number {
    return s.split(' ').filter(w => w).length;
};

