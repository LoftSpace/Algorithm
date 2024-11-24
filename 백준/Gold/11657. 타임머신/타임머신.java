import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static ArrayList<Edge> edges;
	static long[] dist;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		dist = new long[N+1];
		edges = new ArrayList<>();
		
		for(int i=0; i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int u= Integer.parseInt(st.nextToken());
			int v= Integer.parseInt(st.nextToken());
			int cost= Integer.parseInt(st.nextToken());
			edges.add(new Edge(u,v,cost));
		}
		for(int i=1;i<N+1;i++)
			dist[i] = Long.MAX_VALUE;
		if(bellmanFord(1))
			for(int i=2;i<N+1;i++)
				System.out.println(dist[i] == Long.MAX_VALUE? "-1" : dist[i]);
		else
			System.out.println(-1);
	}
	
	static boolean bellmanFord(int start){
		dist[start]=0;
		for(int i=0;i<N-1;i++) {
			for(Edge edge:edges) { //E개 간선 확인 u -> v
				int u = edge.from;
				int v = edge.to;
				if(dist[u] == Long.MAX_VALUE)
					continue;
				if(dist[v] > dist[u] + edge.cost)
					dist[v] = dist[u] + edge.cost;
			}
		}
		
		for(Edge edge : edges) {
			if(dist[edge.from] == Long.MAX_VALUE)
				continue;
			if(dist[edge.to] > dist[edge.from] + edge.cost) {
				
				return false;
			}
		}
		
		return true;
	}

}
class Edge {
	int from;
	int to ;
	int cost;
	public Edge(int from, int to, int cost) {
		
		this.from = from;
		this.to = to;
		this.cost = cost;
	}
	
}