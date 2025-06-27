import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[] standards;
    static int answer = 1;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        standards = new int[M];

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            standards[i] = Integer.parseInt(st.nextToken());
        }

        int temp = 1;
        for(int standard : standards){

            if(standard > 1 && standard > temp){
                int[] arr = new int[standard - temp];
                for(int i = temp; i < standard; i++)
                    arr[i - temp] = i;
                answer *= count(arr);
            }
            temp = standard + 1;
        }
        //마지막 기준점 이후
        if(temp < N){
            int[] arr = new int[N - temp + 1];
            for(int i = temp; i < N; i++){
                arr[i-temp] = i;
            }
            answer *= count(arr);
        }
        System.out.println(answer);
    }

    static int count(int[] arr){
        int arrLength = arr.length;
        int[][] dp = new int[arrLength][3];

        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[0][2] = 0;
        if(arrLength == 1) return 1;
        else if(arrLength == 2) return 2;
        else {
            for (int i = 1; i < arrLength; i++){
                dp[i][0] = dp[i-1][2];
                dp[i][1] = dp[i-1][0] + dp[i-1][1];
                dp[i][2] = dp[i-1][0] + dp[i-1][1];
            }
            return dp[arrLength - 1][0] + dp[arrLength - 1][1] + dp[arrLength - 1][2];
        }

    }
}