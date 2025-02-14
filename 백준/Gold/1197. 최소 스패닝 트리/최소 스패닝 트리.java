import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int V;
    static int E;
    static int[] tree;
    static int answer = 0;
    static PriorityQueue<Edge> pq;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        tree = new int[V + 1];
        pq = new PriorityQueue<>((o1,o2)-> o1.cost - o2.cost);
        init();
        for(int i = 0;i < E ; i ++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            pq.offer(new Edge(u,v,w));
        }

        while(!pq.isEmpty()){
            Edge edge = pq.poll();
            int a = edge.u;
            int b = edge.v;
            int weight = edge.cost;
            if(find(a)==find(b)){
                continue;
            }else {
                union(a,b);
                answer += weight;
            }
        }
        sb.append(answer);
        System.out.println(sb.toString());
    }
    static void init(){
        for(int i = 0; i < V + 1; i ++){
            tree[i] = i;
        }
    }
    static void union(int a,int b){
        int aRoot = find(a);
        int bRoot = find(b);
        tree[aRoot] = bRoot;
    }
    static int find(int a){
        if(a == tree[a])
            return a;
        return tree[a] = find(tree[a]);
    }
}
class Edge implements Comparable<Edge>{
    int u;
    int v;
    int cost;

    public Edge(int u,int v,int cost){
        this.u = u;
        this.v = v;
        this.cost = cost;
    }
    @Override
    public int compareTo(Edge o) {
        return this.cost - o.cost;
    }
}
