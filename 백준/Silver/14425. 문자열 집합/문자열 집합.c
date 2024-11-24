#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define alpha 26

struct Trie
{
	int isleaf;
	struct Trie* character[alpha];
};

struct Trie* getNewTrieNode()  ///새로운 노드생성
{
	struct Trie* node = (struct Trie*)malloc(sizeof(struct Trie));
	node->isleaf = 0;
	for (int i = 0; i < alpha; i++)
		node->character[i] = NULL;
	return node;

}
void insert(struct Trie* head, char* str)  ///문자열 삽입
{
	struct Trie* temp;
	temp = head;

	while (*str)
	{	
		if (temp->character[*str - 'a'] == NULL)
		{
		
			temp->character[*str - 'a'] = getNewTrieNode();
			
		}
		temp = temp->character[*str - 'a'];
		str++;
		
	}
	temp->isleaf = 1; ///단어의 끝임을 알림

}

int search(struct Trie* head, char* str)  ///문자열 찾기
{
	struct Trie* temp = head;
	if (head == NULL)
		return 0;
	while (*str)
	{
		temp = temp->character[*str - 'a'];
		if (temp == NULL)
			return 0;
		str++;
	}
	return temp->isleaf;  ///1반환시 단어의 끝이 일치함을 알리고 0이면 단어가 완전히 일치는 아님ex) sun vs su
}

int main(void)
{	
	int n, m,i,sum=0;
	
	scanf("%d %d", &n, &m);
	char** str1 = (char**)malloc(sizeof(char*) * n);
	char** str2 = (char**)malloc(sizeof(char*) * m);
	for (i = 0; i < n; i++)
		str1[i] = (char*)malloc(sizeof(char) * 500);
	for (i = 0; i < m; i++)
		str2[i] = (char*)malloc(sizeof(char) * 500);
	for (i = 0; i < n; i++)
		scanf("%s", str1[i]);
	
	for (i = 0; i < m; i++)
		scanf("%s", str2[i]);

	struct Trie* Tree=getNewTrieNode();
	
	for (i = 0; i < n; i++)
		insert(Tree, str1[i]);
	

	for (i = 0; i < m; i++)
	{
		sum+=search(Tree, str2[i]);
	}
	printf("%d", sum);
	free(str1);
	free(str2);


	return 0;

}