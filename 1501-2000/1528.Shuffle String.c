char * restoreString(char * s, int* indices, int indicesSize){
    for (int i = 0; i < indicesSize; i++) {
        int j = i;
        while (indices[j] >= 0)
        {
            char tmp = s[i]; s[i] = s[indices[j]]; s[indices[j]] = tmp;
            indices[j] = ~indices[j];
            j = ~indices[j];
        }
    }
    return s;
}