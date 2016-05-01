#pragma warning (disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define bool int
#define false 0
#define true 1
/* Idea: using hash table */
bool isAnagram(char* s, char* t) {
	short hash[26];
	memset(hash, 0, sizeof(short)* 26);
	int count = 0;
	for (char* p = s; *p != '\0'; p++)
	{
		hash[*p - 'a']++;
		count++;
	}
	for (char* p = t; *p != '\0'; p++)
	{
		if (hash[*p - 'a'] <= 0 || count <= 0)
			return false;
		hash[*p - 'a']--;
		count--;
	}
	if (count != 0)
		return false;
	return true;
}