
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[][] dpMax = new int[N + 1][3];
        int[][] dpMin = new int[N + 1][3];
        int[][] arr = new int[N + 1][3];

        for(int i = 1; i < N  + 1; i ++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            arr[i][0] = a;
            arr[i][1] = b;
            arr[i][2] = c;


        }
        for(int i = 0; i < N  +1; i ++){
            for(int j = 0; j < 3; j++){
                dpMin[i][j] = 10000000;
            }
        }
        dpMax[1][0] = arr[1][0];
        dpMax[1][1] = arr[1][1];
        dpMax[1][2] = arr[1][2];
        dpMin[1][0] = arr[1][0];
        dpMin[1][1] = arr[1][1];
        dpMin[1][2] = arr[1][2];
        for(int i = 2 ; i <= N; i++){
            for(int j = 0; j < 3; j++){
                dpMax[i][j] = Math.max(dpMax[i][j],dpMax[i-1][j]);
                dpMin[i][j] = Math.min(dpMin[i][j],dpMin[i-1][j]);
                if(j - 1 >= 0) {
                    dpMax[i][j] = Math.max(dpMax[i][j], dpMax[i - 1][j - 1]);
                    dpMin[i][j] = Math.min(dpMin[i][j],dpMin[i-1][j-1]);
                }
                if(j + 1 < 3) {
                    dpMax[i][j] = Math.max(dpMax[i][j], dpMax[i - 1][j + 1]);
                    dpMin[i][j] = Math.min(dpMin[i][j],dpMin[i-1][j+1]);
                }

                dpMax[i][j] += arr[i][j];
                dpMin[i][j] += arr[i][j];
            }
        }

        int answer1 = 0;
        int answer2 = Integer.MAX_VALUE;
        for(int i = 0; i <3; i ++){
            answer1 = Math.max(answer1,dpMax[N][i]);
            answer2 = Math.min(answer2,dpMin[N][i]);
        }

        System.out.println(answer1 + " " + answer2);
    }
}
