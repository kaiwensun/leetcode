int numberOfSteps (int num){
    int res;
    for (res = 0; num; res ++) {
        if (num & 1) num -= 1;
        else num >>= 1;
    }
    return res;
}
