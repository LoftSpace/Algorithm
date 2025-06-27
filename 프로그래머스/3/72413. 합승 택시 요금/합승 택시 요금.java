import java.util.*;
class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = 100000000;
        int[][] graph = new int[n + 1][n + 1];
        for(int i = 0 ; i < n + 1; i++)
            for(int j = 0; j < n + 1; j++)
                graph[i][j] = 300000000;
        for(int i = 0; i < n + 1; i++)
            graph[i][i] = 0;
        
        Map<Integer,List<Edge>> edges = new HashMap<>();
        for(int i = 1; i < n + 1; i++)
            edges.put(i,new ArrayList<>());
        
        for(int[] edge : fares){
            int u = edge[0];
            int v = edge[1];
            int cost = edge[2];
            edges.get(u).add(new Edge(v,cost));
            edges.get(v).add(new Edge(u,cost));
            graph[u][v] = cost;
            graph[v][u] = cost;
        }
        
        for(int k = 1; k <= n; k ++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                    graph[i][j] = Math.min(graph[i][j],graph[i][k] + graph[k][j]);
                }
            }
        }
       // int totalCost = 0;
        for(int midPoint = 1; midPoint <= n; midPoint++){
            answer = Math.min(answer,graph[s][midPoint] + graph[midPoint][a] + graph[midPoint][b]);
        }
        return answer;
    }
}
class Edge{
    int to;
    int cost;
    public Edge(int to, int cost){
        this.to = to;
        this.cost = cost;
    }
}