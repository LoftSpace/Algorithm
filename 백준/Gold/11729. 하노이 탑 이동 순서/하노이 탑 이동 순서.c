#include <stdio.h>
#include <math.h>
int k = 0;

void mover(int* a) ///원판을 낄때 자리만들기
{
	int i = 0,temp,j=a[0];
	
	while (a[i] != -1)
	{
		if (i == 19)
			return;
		temp = a[i + 1];
		a[i + 1] = j;
		j = temp;
		i++;
	}
}
void movel(int* a) ///원판을 뺏을때
{
	int i = 0;
	while (a[i] != -1)
	{
		if (i == 19)
			return;
		a[i] = a[i + 1];
		i++;
		
	}	
}
///1->3으로 n개옮김
void hanoi(int n,int* a,int* b,int* c) ///a를 c로  원판 이동
{
	if (n == 1)
	{
		mover(c);
		c[0] = a[0];
		movel(a);
		printf("%d %d\n", a[20], c[20]);
		k++;
		return;
	}
	hanoi(n - 1, a, c, b); ///1->2로 n-1개옮김
	hanoi(1, a, b, c);  ///1->3으로 1개옮김
	hanoi(n - 1, b, a, c); ///2->3으로 n-1개옮김

}

int main(void)
{
	int n,i;
	int load1[21] , load2[21] , load3[21] ;
	for (i = 0; i < 20; i++)
	{
		load1[i] = -1;
		load2[i] = -1;
		load3[i] = -1;
	}
	load1[20] = 1;
	load2[20] = 2;
	load3[20] = 3;
	scanf(" %d", &n);
	printf("%.0f\n", (pow(2,n)) - 1);
	for (i = 0; i <n; i++)
		load1[i]=i;
	hanoi(n,load1,load2, load3);
	
	return 0;

}