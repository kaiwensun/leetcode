/*
 * Result:
 *    476 / 476 test cases passed.
 *    Status: Accepted
 *    Runtime: 4 ms
 * Date:
 *    5/1/2016
 */
char* reverseString(char* s) {
    if(s==NULL)return s;
    char* l = s;
    char* r = s+strlen(s)-1;
    while(l<r){
        char t = *l;*l++=*r;*r--=t;
    }
    return s;
}
