import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N + 1][N + 1];
      
        for(int i = 1; i < N + 1; i++)
            for(int j = 1; j < N + 1; j++) {
                graph[i][j] = 100_000_000;
                if(i == j)
                    graph[i][j] = 0;
            }

        for(int i = 1; i <= M; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u][v] = w;
            
        }

        for(int k = 1; k < N + 1; k++){
            for(int a = 1; a < N + 1; a++){
                for(int b = 1; b < N + 1; b++){
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }
        
        int ans = 0;
        for(int i = 1; i < N + 1; i ++){
            int time = 0;
            time += graph[i][X];
            time += graph[X][i];
            ans = Math.max(ans,time);
        }
        System.out.println(ans);
    }
}
