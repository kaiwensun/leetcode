/*
 * Result:
 *    481 / 481 test cases passed.
 *    Status: Accepted
 *    Runtime: 4 ms
 * Date: 
 *    5/1/2016
 */
#include<string.h>
bool isVowel(char c) {
    switch(c){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            return true;
        default:
            return false;
    }
}
char* reverseVowels(char* s) {
    if(s==NULL)
        return NULL;
    char* l = s;
    char* r = s+strlen(s)-1;
    while(l<r){
        while(l<r && !isVowel(*l)) l++;
        while(l<r && !isVowel(*r)) r--;
        char tmp = *l;*l=*r;*r=tmp;
        l++;r--;
    }
    return s;
}
