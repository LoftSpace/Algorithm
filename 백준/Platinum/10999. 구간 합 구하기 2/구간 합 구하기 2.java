import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int S;
	static long[] elements, tree, lazy;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		elements = new long[N];
		
		
		S= 1 ;
		while( S < N) {
			S *= 2;
		}
		
		tree = new long[S * 2];
		lazy = new long[S * 2];
		for(int i=0; i<N; i++) {
			tree[i +  S] = Long.parseLong(br.readLine());
		}
		
		init();
		
		for(int i = 0; i< M + K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			if(a == 1 ) {
				long d = Long.parseLong(st.nextToken());
				update(1,1,S,b,c,d);
			} else {
				System.out.println(sum(1,1,S,b,c));
			}
			/*
			for(int j=0; j<2 *S ; j++) {
				System.out.print(tree[j] + " ");
			}
			System.out.println();
			*/
		}
	}
	
	static void init() {
		for(int i = S - 1; i > 0; i--)
			tree[i] =tree[i * 2] + tree[i * 2 + 1];
	}
	static void update(int node, int left, int right, int queryLeft, int queryRight, long diff) {
		propagate(node,left,right);
		if(queryLeft > right || queryRight < left) return;
		
		if(queryLeft <= left && right <= queryRight) {
			tree[node] += (right - left + 1) * diff;
			if(left != right) {
				lazy[node * 2] += diff;
				lazy[node*2 + 1] += diff;
			}
			return ;
		}
		
		int mid = (left + right) / 2;
		update(node * 2,left, mid,queryLeft,queryRight,diff);
		update(node * 2 + 1,mid + 1,right,queryLeft,queryRight,diff);
		tree[node] = tree[node * 2] + tree[node * 2 + 1];
	}
	static void propagate(int node,int left,int right) {
		if(lazy[node] !=0) {
			tree[node] += (right - left + 1) * lazy[node];
			
			if(left != right) {
				lazy[node * 2] += lazy[node];
				lazy[node * 2 + 1] += lazy[node];
			}
			lazy[node] = 0;
		}
	}
	static long sum(int node, int left, int right, int queryLeft, int queryRight) {
		propagate(node,left,right);
		if(queryLeft > right || queryRight < left) return 0;
		if(queryLeft <= left && queryRight >= right) return tree[node];
		
		int mid = (left + right) / 2;
		return sum(node * 2, left, mid, queryLeft, queryRight) + sum(node * 2 + 1, mid + 1, right, queryLeft, queryRight);
	}
	
}
