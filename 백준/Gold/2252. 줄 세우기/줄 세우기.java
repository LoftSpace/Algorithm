import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N , M;
	static int[] indegree;

	static ArrayList<Integer> adjList = new ArrayList<>();
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	public static StringBuilder sb = new StringBuilder();
	static Queue<Integer> queue = new LinkedList<>();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
	
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a,b;
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			indegree = new int[N+1];
		
			
			for(int i=0;i<N+1;i++) {
				indegree[i]=0;
			
			}
			for (int i = 0; i <= N+1; i++) {
	            graph.add(new ArrayList<>());
	        }
			
			for(int i=0;i<M;i++) {
				st = new StringTokenizer(br.readLine());
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				graph.get(a).add(b);
				indegree[b]++;
				
			}
			//topologicalSort();
			for(int i=1;i<N+1;i++) {
				if(indegree[i]==0) {
					queue.offer(i);
				}
			}
			int index;
			int next;
			while(!queue.isEmpty()) {
				 index = (int) queue.poll();
				
				for(Integer i : graph.get(index)) {
					indegree[i]--;
					if(indegree[i]==0) {
						queue.offer(i);
					}
				}
				sb.append(index + " ");
			
			}
			
			System.out.println(sb);
			
	}
	public static void topologicalSort() {
		int node = queue.poll();
		
	}
}
