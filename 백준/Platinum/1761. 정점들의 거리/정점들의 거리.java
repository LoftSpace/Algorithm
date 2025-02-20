import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int H;
	static int[] depths;
	static int[] distance;
	static int[][] parents;
	static ArrayList<Node>[] tree;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		tree = new ArrayList[N + 1];
		
		for(int i=0; i < N + 1; i++) {
			tree[i] = new ArrayList<>();
		}
		
		for(int i = 0; i < N - 1; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			tree[from].add(new Node(to,weight));
			tree[to].add(new Node(from,weight));
		}
		getHeight();
		init();
		setParent(1,1,0);
		setAllParents();
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		for(int i = 0; i <n; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int start = LCA(u,v);
			System.out.println(distance[u] + distance[v] - 2 * distance[start]);
		}
		
	}
	static int track(int from,int to) {
		return distance[to] - distance[from];
		
	}
	static void init() {
		depths = new int[N + 1];
		distance = new int[N + 1];
		parents = new int[N + 1][H];
	}
	static void setParent(int cur, int h, int pa) {
		depths[cur] = h;
		for(Node next : tree[cur]) {
			if(next.to != pa) {
				distance[next.to] = next.weight + distance[cur];
				setParent(next.to,h + 1,cur);
				parents[next.to][0] = cur;
			}
		}
	}
	static void setAllParents() {
		for(int j = 1; j < H; j++)
			for(int i = 1; i < N  +1; i++ )
				parents[i][j] = parents[parents[i][j-1]][j-1];
	}
	
	static int LCA(int a, int b) {
		if(depths[a] < depths[b]) {
			int temp = a;
			a = b;
			b = temp;
		}
		
		for(int i = H-1; i >= 0; i--) {
			if(Math.pow(2, i) <= depths[a] - depths[b])
				a = parents[a][i];
		}
		
		if(a == b)
			return a;
		
		for(int i = H - 1; i>=0; i--) {
			if(parents[a][i] != parents[b][i]) {
				a = parents[a][i];
				b = parents[b][i];
			}
				
		}
		return parents[a][0];
	}
	static void getHeight() {
		H = (int)Math.ceil(Math.log(N)/Math.log(2)) + 1;
	}

}
class Node implements Comparable<Node>{
	int to;
	int weight;
	public Node(int to, int weight) {
		this.to = to;
		this.weight = weight;
	}
	@Override
	public int compareTo(Node o) {
		return this.weight - o.weight;
	}
}