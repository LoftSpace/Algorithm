#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int k = 0;
int recursion(char* s, int l, int r,int * m)
{
	m[k]++;
	if (l >= r)
		return 1;
	else if (s[l] != s[r])
		return 0;
	else return recursion(s, l + 1, r - 1,m);
}


int isPalindrome(char*s,int *m)
{
	k++;
	return recursion(s, 0, strlen(s) - 1,m);
}


int main(void)
{
	int n,i;
	scanf("%d", &n);
	int* m = (int*)malloc(sizeof(int) * (n+1));
	char** s = (char**)malloc(sizeof(char*) * n);
	for (i = 0; i < n; i++)
	{
		m[i] = 0;
		s[i] = (char*)malloc(sizeof(char) * 1001);
		scanf(" %s", s[i], sizeof(char)*1001);
	}
	m[n] = 0;
	for (i = 0; i < n; i++)
	{
		int a = isPalindrome(s[i], m);
		printf("%d %d\n", a, m[i+1]);
	}
	
	return 0;
}