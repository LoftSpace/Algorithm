import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int S;
	static long[] tree;
	static long[] lazy;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());
		S = 1;
		
		while( S < N)
			S *= 2;
		tree = new long[S * 2];
		lazy = new long[S * 2];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i ++)
			tree[S + i] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		for(int i = 0; i < M; i ++) {
			st = new StringTokenizer(br.readLine());
			int operation = Integer.parseInt(st.nextToken());
			if(operation == 1) {
				int queryLeft = Integer.parseInt(st.nextToken());
				int queryRight = Integer.parseInt(st.nextToken());
				long diff = Long.parseLong(st.nextToken());
				update(1,1,S,queryLeft,queryRight,diff);
			}else {
				int x = Integer.parseInt(st.nextToken());
				sb.append(query(1,1,S,x) + "\n");
			}
		}
		System.out.print(sb.toString());
		
	}
	static void init() {
		for(int i = S-1; i > 0; i--)
			tree[i] = tree[i * 2] + tree[i*2+1];
	}
	static long query(int node,int left,int right,int target) {
		propagate(node,left,right);
		if(target < left || right < target) return 0;
		else if(target == left && target == right) return tree[node];
		else {
			int mid = (left + right) / 2;
			return query(node * 2,left,mid,target) + query(node * 2 + 1,mid + 1,right,target);
		}
	}
	static void propagate(int node,int left,int right) {
		if(lazy[node] != 0) {
			tree[node] += lazy[node];
			if(left != right) {
				lazy[node*2] += lazy[node];
				lazy[node * 2 + 1] += lazy[node];
			}
		}
		lazy[node] = 0;
	}
	static void update(int node,int left, int right, int queryLeft, int queryRight, long diff ) {
		propagate(node,left,right);
		if(right < queryLeft || queryRight < left) return;
		else if (queryLeft <= left && right <= queryRight) {
			tree[node] += diff;
			if(left != right) {
				lazy[node * 2] += diff;
				lazy[node * 2 + 1] += diff;
			}
		}
		else {
			int mid = (left + right) / 2;
			update(node * 2,left,mid, queryLeft,queryRight,diff);
			update(node * 2 + 1,mid + 1,right, queryLeft,queryRight,diff);
			tree[node]  = tree[node * 2] + tree[node * 2  +1];
		}
	}
		
	
}
