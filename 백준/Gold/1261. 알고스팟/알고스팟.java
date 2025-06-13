import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static PriorityQueue<Node> pq = new PriorityQueue<>();
    static ArrayList<Node>[] graph;
    static int[][] map;
    static boolean[] visited;
    static int[] dist;
    static int[] dRow = {1,-1,0,0};
    static int[] dCol = {0,0,1,-1};
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited=  new boolean[N * M];
        dist = new int[N * M];
        graph = new ArrayList[N * M];
        for(int i = 0; i < N * M; i++) {
            dist[i] = 100000000;
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < N; i++){
            String s = br.readLine();
            for(int j = 0; j < s.length(); j++){
                map[i][j] = s.charAt(j) - '0';
            }

        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M;j++){
                for(int dir = 0 ; dir < 4; dir++){
                    int nextRow = i + dRow[dir];
                    int nextCol = j + dCol[dir];
                    if(0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < M){
                        if(map[nextRow][nextCol] == 1)
                            graph[i * M + j].add(new Node(nextRow * M + nextCol,100000));
                        else
                            graph[i * M + j].add(new Node(nextRow * M + nextCol,1));
                    }
                }
            }
        }

        dist[0] = 0;
        dijkstra();
        System.out.println(dist[N * M - 1] / 100000);
    }

    static void dijkstra(){
        pq.add(new Node(0,0));

        while(!pq.isEmpty()){
            Node node = pq.poll();
            if(!visited[node.node]){
                visited[node.node] = true;
            }

            for(Node nextNode : graph[node.node]){

                if(!visited[nextNode.node] && dist[nextNode.node] > node.cost + nextNode.cost){
                    dist[nextNode.node] = node.cost + nextNode.cost;
                    pq.add(new Node(nextNode.node, dist[nextNode.node]));
                }
            }
        }
    }

}

class Node implements Comparable<Node>{

    int node;
    int cost;
    public Node( int node, int cost){

        this.node = node;
        this.cost = cost;
    }
    @Override
    public int compareTo(Node o){
        return this.cost - o.cost;
    }
}