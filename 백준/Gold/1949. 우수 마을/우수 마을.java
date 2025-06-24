import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static int[] V;
    static boolean[] visited;
    static int[][] dp;
    static Map<Integer, List<Integer>> graph = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        V = new int[N + 1];
        visited = new boolean[N +1];
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i < N + 1;i++)
            V[i] = Integer.parseInt(st.nextToken());


        for(int i = 1; i < N + 1; i++)
            graph.put(i,new ArrayList<>());
        for(int i = 0; i < N - 1; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        dp = new int[N + 1][2];
        dfs(1);
        System.out.println(Math.max(dp[1][0],dp[1][1]));
    }

    static void dfs(int node){
        visited[node] = true;
        dp[node][0] = 0;
        dp[node][1] = V[node];
        for(int nextNode : graph.get(node)){
            if(visited[nextNode]) continue;

            dfs(nextNode);

            dp[node][1] += (dp[nextNode][0]);
            dp[node][0] += (Math.max(dp[nextNode][1],dp[nextNode][0]));
        }
    }
}
