int countSeniors(char ** details, int detailsSize){
    int res = 0;
    for (int i = 0; i < detailsSize; i++) {
        details[i][13] = '\0';
        if ((details[i][11] - '0') * 10 + details[i][12] - '0' > 60) res++;
    }
    return res;
}

