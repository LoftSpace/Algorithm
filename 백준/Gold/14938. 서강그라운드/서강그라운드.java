import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Map<Integer,List<Node>> graph = new HashMap<>();
    static int answer = 0;
    static int[] dist;
    static boolean[] visited;
    static int N, M, E;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        dist = new int[N + 1];
        visited = new boolean[N + 1];
        int[] items = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for(int i = 1; i < N + 1; i++) {
            items[i] = Integer.parseInt(st.nextToken());
            graph.put(i, new ArrayList<>());
        }

        for(int i = 0; i < E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph.get(u).add(new Node(v,cost));
            graph.get(v).add(new Node(u,cost));
        }

        for(int startNode = 1; startNode < N + 1; startNode++){
            init();
            int count = 0;
            dijkstra(startNode);
            for(int nextNode = 1; nextNode < N + 1; nextNode++){
                if(dist[nextNode] <= M)
                    count += items[nextNode];
            }

            answer = Math.max(answer,count);
        }

        System.out.println(answer);
    }

    static void dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> o1.cost - o2.cost);
        dist[start] = 0;

        pq.add(new Node(start,0));

        while(!pq.isEmpty()){
            Node node = pq.poll();
            if(!visited[node.node]) {
                visited[node.node] = true;

                if (dist[node.node] < node.cost) continue;

                for (Node nextNode : graph.get(node.node)) {
                    if (!visited[nextNode.node] && dist[nextNode.node] > dist[node.node] + nextNode.cost) {
                        dist[nextNode.node] = dist[node.node] + nextNode.cost;
                        pq.add(new Node(nextNode.node, dist[nextNode.node]));
                    }
                }
            }
        }

    }
    static void init(){
        for(int i = 1; i < N + 1; i ++){
            visited[i] = false;
            dist[i] = 1000000;
        }
    }
}

class Node {
    int node;
    int cost;
    public Node(int node,int cost){
        this.node = node;
        this.cost = cost;
    }
}