#include <stdio.h>
int multi(int n)
{
	if(n!=0)
		return multi(n - 1) * n;
	if(n==0)
		return 1;
}
int main(void)
{
	int n;
	scanf("%d", &n);
	printf("%d", multi(n));
}