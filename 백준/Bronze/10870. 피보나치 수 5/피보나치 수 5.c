#include <stdio.h>  ///피보나치

int func(int n)
{
	if (n == 1)
		return 0;
	if (n == 2)
		return 1;

	return func(n - 1) + func(n - 2);
}

int main(void)
{
	int n;
	scanf("%d", &n);
	printf("%d", func(n+1));
	return 0;
}