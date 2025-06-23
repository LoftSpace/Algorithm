import java.util.*;
class Solution {
    static Map<Integer,List<Integer>> graph = new HashMap<>();
    static int answer = 0;
    static int[][] dp;
    static boolean[] visited;
    public int solution(int n, int[][] lighthouse) {
        visited = new boolean[n + 1];
        dp = new int[n + 1][2];
        
        for(int i = 1; i < n + 1; i++){
            graph.put(i,new ArrayList<>());
        }
        
        for(int[] edge : lighthouse){
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        
        dfs(1);
        int answer = Math.min(dp[1][0],dp[1][1]);
        return answer;
    }
    static void dfs(int node){
        dp[node][0] = 0;
        dp[node][1] = 1;
        visited[node] = true;
        
        for(int nextNode : graph.get(node)){
            if(visited[nextNode]) continue;
            
            dfs(nextNode);
            
            dp[node][0] += dp[nextNode][1];
            dp[node][1] += Math.min(dp[nextNode][0],dp[nextNode][1]);
        }
    }
}