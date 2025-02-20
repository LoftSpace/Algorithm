import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int S;
	static long ans =0;
	static int[] A;
	static long[] tree;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		HashMap<Integer,Integer> hash = new HashMap<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		A = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++)
			A[i] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++)
			hash.put(Integer.parseInt(st.nextToken()), i);
		S = 1;
		while(S < N)
			S *= 2;
		tree = new long[S * 2 + 1];
		
		for(int i = 0; i < N; i ++) {
			// query left : hash[A[i]] ~ S
			int b = hash.get(A[i]);
			update(1,1,S,b + 1,1);
			ans += query(1,1,S,b + 2,S);
			
			// update target : hash[A[i]], diff = 1
		}
		System.out.println(ans);
	}
	static long query(int node, int left, int right,int queryLeft, int queryRight) {
		if(right < queryLeft || queryRight < left) return 0;
		else if(queryLeft <= left && right <= queryRight) return tree[node];
		else {
			int mid = (left + right) / 2;
			return query(node * 2,left,mid,queryLeft,queryRight) + query(node * 2 + 1,mid + 1,right,queryLeft,queryRight);
		}
	}
	static void update(int node, int left, int right, int target, long diff) {
		if(target < left || right < target) return;
		tree[node] += diff;
		if(left != right) {
			int mid = (left + right) / 2;
			update(node * 2,left,mid,target,diff);
			update(node * 2 + 1,mid + 1,right,target,diff);
		}
	}
	
}
