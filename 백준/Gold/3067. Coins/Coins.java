import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int T = Integer.parseInt(st.nextToken());

        for(int tc = 0; tc < T; tc++){
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[] coins = new int[N];
            int MaxCoin = 0;
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i++){
                int coin = Integer.parseInt(st.nextToken());

                coins[i] = coin;
            }

            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int[] dp = new int[M + 1];
            dp[0] = 1;

            for(int coin : coins){
                for(int i = coin; i < M + 1; i++){
                    dp[i] += dp[i - coin];
                }
            }

            System.out.println(dp[M]);
        }
    }
}