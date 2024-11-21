#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


long long Day = 0;
int main(void)
{
	long long n,t,num,day;
	long long temp,tday;
	scanf("%lld %lld", &n, &t);
	
	scanf("%lld %lld", &day, &num);
	tday = day;
	temp = num;
	
	for (int i = 0; i < n-1; i++)
	{
		scanf("%lld %lld", &day, &num);
		if (day - tday + 1 < temp)
		{
			Day += day - tday;
			temp = num + temp - (day - tday);
			tday = day;
		
			
		}
		else
		{
			Day += temp;
			temp = num;
			tday = day;
		}
		
	}
	if (temp > 0 && t == tday)
		Day++;
	else if (temp > t - tday + 1)
		Day += t - tday + 1;
	else if (temp <= t - tday + 1)
		Day += temp;
		
	
	printf("%lld", Day);
	
	return 0;
}