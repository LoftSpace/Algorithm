#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>


int main(void)
{
	
	long long city, * road, * oil;
	scanf("%lld", &city);
	oil = (long long*)malloc(sizeof(long long) * city);
	road = (long long*)malloc(sizeof(long long) * (city - 1));
	int i, temp = 0, k = 1;
	long long min, sum = 0;
	
	for (i = 0; i < city - 1; i++)
		scanf("%lld", &road[i]);
	for (i = 0; i < city; i++)
		scanf("%lld", &oil[i]);
	min = oil[0];
	for (i = 0; i < city - 1; i++)
	{
		if (oil[i] <= min)
			min = oil[i];
		
		sum += road[i] * min;
	}
	
	printf("%lld", sum);
	return 0;

}