#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	long long N, K;
	scanf("%lld %lld", &N, &K);
	long long* ns = (long long*)malloc(sizeof(long long) * N);
	long long cost = 0;
	for (long long i = 0; i < N; i++)
		scanf("%lld", &ns[i]);
	cost += K + 1;
	if (N == 1) ///날짜가 1개
		printf("%lld",cost);
	else
	{
		for (long long i = 1; i < N; i++)
		{
			if (ns[i] - ns[i - 1] <= K) ///연장
				cost += ns[i] - ns[i - 1] ;
			else ///구독기간 끝
				cost += K + 1;
		}
		printf("%lld", cost);
	}
	
	return 0;
}