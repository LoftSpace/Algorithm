#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int check(char* block, char* vocab, int a)
{
	int i;
	
	for (i = 0; i < 6; i++)
	{
		
		if (block[i] == vocab[a])
		{
			return 1;
		}
	}
	
	return 0;
}
int check2(char* arr,char** block,int n)   ///
{
	int i,j;
	int visit[4] = { 0 };
	for (i = 0; i < n; i++)
	{
		int c = 0;
		int cc = 0;
		for (j = 0; j < 4; j++)
		{
			if (c == 0 && visit[j]==0)
			{
				if (check(block[j], arr, i) == 1) ///글자가 블록에 있으면,
				{
					c = 1;
					visit[j] = 1;
					cc = 1;
				}
			}
		}
		if (cc == 0) ///글자가 4개블록 전부에도 없으면,
			return 0;
	}
	return 1;
}
void func1(char** block, char* vocab)
{
	int j;
	if (check2(vocab, block, 1) == 1)
		printf("YES\n");
	else
		printf("NO\n");
}
void func2(char** block, char* vocab)
{
	int i, j;
	char arr[2];
	int temp = 0;
	for(i=0;i<2;i++)
		for (j = 0; j < 2; j++)
		{
			arr[0] = vocab[i];
			arr[1] = vocab[j];
			if (i != j)
			{
				if (check2(arr, block, 2) == 1)
				{
					temp = 1;
				}
			}
		}
	if (temp == 1)
		printf("YES\n");
	else
		printf("NO\n");
}
void func3(char** block, char* vocab)
{
	int i, j, k;
	char arr[3];
	int temp = 0;
	for (i = 0; i < 3; i++)
		for (j = 0; j < 3; j++)
			for (k = 0; k < 3; k++)
			{
				arr[0] = vocab[i];
				arr[1] = vocab[j];
				arr[2] = vocab[k];
				if (i != j && i != k && j != k)
				{
					
					if (check2(arr, block, 3) == 1)
					{
						temp = 1;
					}	
				}
			}
	if (temp == 1)
		printf("YES\n");
	else
		printf("NO\n");
}
void func4(char** block, char* vocab)
{
	int i, j, k,l;
	char arr[4];
	int temp = 0;
	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			for (k = 0; k < 4; k++)
			{
				for (l = 0; l < 4; l++)
				{
					arr[0] = vocab[i];
					arr[1] = vocab[j];
					arr[2] = vocab[k];
					arr[3] = vocab[l];
					if (i != j && i != k && i != l)
					{
						if (j != k && j != l && k != l)
						{
							if (check2(arr, block, 4) == 1)
							{
								temp = 1;
							}
						}
					}
				}
			}
	if (temp == 1)
		printf("YES\n");
	else
		printf("NO\n");
}
int main(void)
{
	char** blocks=(char**)malloc(sizeof(char*)*4);
	
	int i,n;
	for (i = 0; i < 4; i++)
	{
		blocks[i] = (char*)malloc(sizeof(char) * 7);
	}
	char characters[26];
	scanf("%d", &n);
	char** vocab = (char**)malloc(sizeof(char*) * n);
	for (i = 0; i < n; i++)
		vocab[i] = (char*)malloc(sizeof(int) * 5);
	for (i = 0; i < 4; i++)
		scanf("%s", blocks[i]);
	
	for (i = 0; i < n; i++)
	{
		scanf("%s", vocab[i]);
	}
	  ///// 세팅 끝 아래부터 알고리즘
	for (i = 0; i < n; i++)
	{
		if (strlen(vocab[i]) == 3)
			func3(blocks, vocab[i]);
		else if (strlen(vocab[i]) == 4)
			func4(blocks, vocab[i]);
		else if (strlen(vocab[i]) == 2)
			func2(blocks, vocab[i]);
		else
			func1(blocks, vocab[i]);

	}
	

	return 0;
}