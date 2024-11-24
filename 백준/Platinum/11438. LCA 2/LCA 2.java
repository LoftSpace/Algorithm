import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static int[][] parent;
	static int[] depth;
	static ArrayList<Integer>[] adjList;
	static boolean[] visited;
	static final int LOG = 17;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		 StringTokenizer st;
		 N = Integer.parseInt(br.readLine());
		 
		 adjList= new ArrayList[N+1];
		 for(int i=1;i<N+1;i++)
			 adjList[i] = new ArrayList<>();
		 visited = new boolean[N+1];
		 depth = new int[N+1];
		 parent = new int[LOG+1][N+1];
		 
		 for(int i=0;i<N-1;i++) {
			 st = new StringTokenizer(br.readLine());
			 int u = Integer.parseInt(st.nextToken());
			 int v = Integer.parseInt(st.nextToken());
			 adjList[u].add(v);
			 adjList[v].add(u);
		 }
		 
		bfs(1);
		
		findAncestor();
		
		 st = new StringTokenizer(br.readLine());
		 M = Integer.parseInt(st.nextToken());
		 
		 StringBuilder sb = new StringBuilder();
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			sb.append(LCA(a,b));
			sb.append('\n');
		}
		 bw.write(sb.toString());
	        bw.flush();
	        bw.close();
	}
	
	
	static void bfs(int root) {
		ArrayDeque<Integer> queue = new ArrayDeque();
		queue.add(root);
		visited[root] = true;
		
		while(!queue.isEmpty()) {
			int currNode = queue.poll();
			
			for(int nextNode : adjList[currNode] ) {
				if(!visited[nextNode]) {
					visited[nextNode] = true;
					queue.add(nextNode);
					parent[0][nextNode] = currNode;
					depth[nextNode] = depth[currNode] + 1; 
				}
			}
		}
	}
	static void findAncestor() {
		for(int k=1;k<=LOG;k++) {
			for(int v=1;v<=N;v++) {
				parent[k][v] = parent[k-1][parent[k-1][v]];
			}
		}
	}
	static int LCA(int a, int b) {
		int temp;
		if(depth[a] > depth[b]) {
			temp=a;
			a=b;
			b=temp;
		}
		
		for(int k=LOG; k>=0;k--) {
			if(depth[b]-depth[a] >= (1<< k)) {
				b=parent[k][b];
			}
		}
		
		if(a==b)
			return a;
		
		for(int k=LOG;k>=0;k--) {
			if(parent[k][a]!=parent[k][b]) {
				a=parent[k][a];
				b=parent[k][b];
			}
		}
		return parent[0][a];
			
	}
}