int distMoney(int money, int children){
    if (money < children) {
        return -1;
    } else if (children * 8 < money) {
        return children - 1;
    } else if (children * 8 - 4 == money) {
        return children - 2;
    } else {
        return (money - children) / 7;
    }
}

