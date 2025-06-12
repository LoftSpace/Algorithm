import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] dp = new int[K + 1][N  +1];
        int[] W = new int[K + 1];
        int[] V = new int[K + 1];

        for(int i = 1; i < K + 1; i++){
            st = new StringTokenizer(br.readLine());
            V[i] = Integer.parseInt(st.nextToken());
            W[i] = Integer.parseInt(st.nextToken());
        }

        //각 과목에 대해
        for(int i = 1; i < K + 1; i++)
            //각 공부 시간에 대해
            for(int j = 1; j < N + 1; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - W[i] >= 0)
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]);
            }

        System.out.println(dp[K][N]);
    }
}