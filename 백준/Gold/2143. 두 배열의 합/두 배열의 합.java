import java.io.*;
import java.util.*;

public class Main {
    static long answer = 0;
    static int T;
    static int N;
    static int M;
    static int[] A;
    static int[] A_SUM;
    static int[] A_COMBINATION;
    static int[] B;
    static int[] B_SUM;
    static int[] B_COMBINATION;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        A = new int[N];
        A_SUM = new int[N + 1];
        A_COMBINATION = new int[N*(N + 1) / 2];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++)
            A[i] = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        B = new int[M];
        B_SUM = new int[M + 1];
        B_COMBINATION = new int[M * (M + 1) / 2];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++)
            B[i] = Integer.parseInt(st.nextToken());


        //누적합 생성
        A_SUM[0] = 0;
        B_SUM[0] = 0;
        for(int i = 1; i < N + 1; i ++)
            A_SUM[i] = A_SUM[i-1] + A[i-1];
        for(int i = 1; i < M + 1; i++)
            B_SUM[i] = B_SUM[i-1] + B[i-1];

        int temp = 0;
        for(int i = 0; i < N; i++){
            for(int j = i + 1; j < N + 1; j++){
                A_COMBINATION[temp++] = A_SUM[j] - A_SUM[i];
            }
        }
        temp = 0;
        for(int i = 0; i < M; i++)
            for(int j = i  + 1; j < M + 1; j++)
                B_COMBINATION[temp++] = B_SUM[j] - B_SUM[i];
        Arrays.sort(A_COMBINATION);

        for(int i = 0; i < M * (M + 1) / 2; i++){
            int target = T - B_COMBINATION[i];
            int start = 0;
            int end = 0;
            int left = 0;
            int right = A_COMBINATION.length - 1;
            //lower bound
            while(left <= right){
                int mid = (left + right) / 2;
                if(A_COMBINATION[mid] == target)
                    right = mid - 1;
                else if(A_COMBINATION[mid] < target)
                    left = mid + 1;
                else
                    right = mid - 1;
            }
            start = left;
            left = 0;
            right = A_COMBINATION.length - 1;
            //upper bound
            while(left <= right){
                int mid = (left + right) / 2;
                if(A_COMBINATION[mid] == target)
                    left = mid + 1;
                else if(A_COMBINATION[mid] < target)
                    left = mid + 1;
                else
                    right = mid - 1;
            }
            end = (right + 1);
            answer += (end - start);
        }
        System.out.println(answer);
    }
}