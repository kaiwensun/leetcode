bool isReachableAtTime(int sx, int sy, int fx, int fy, int t){
    return abs(sx - fx) <= t && abs(sy - fy) <= t && (t != 1 || sx != fx || sy != fy);
}

