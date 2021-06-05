int twoEggDrop(int n){
    int sum = 0, res = 0;
    while ((sum += res++) < n);
    return res - 1;
}

