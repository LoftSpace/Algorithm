
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String s = br.readLine();
        int[] arr = new int[N];
        int[] rightBig = new int[N];
        Stack<int[]> stack = new Stack<>();
        for(int i = 0; i < N; i++){
            arr[i] = s.charAt(i) - '0';
        }

        for(int i = 0; i < N;i++){
            rightBig[i] = -1;
        }
        for(int i = 0; i < N; i++){
            int[] element = {arr[i],i};
            while(!stack.isEmpty() && stack.peek()[0] < element[0]){
                int[] pop = stack.pop();
                rightBig[pop[1]] = element[1];
            }
            stack.push(element);
        }

        int target = N - K;
        int[] answers = new int[N];
        int point = 0;

        for(int i = 0; i < N; i++){
            int j = rightBig[i];
            // 남은 것들 중에 가장 큰 원소면
            if(j == -1){
                answers[point++] = arr[i];
                continue;
            }
            // 패스
            if(N - j >= target - point) continue;

            answers[point++] = arr[i];
        }

        for(int i = 0; i < target; i++){
            sb.append(answers[i]);
        }

        System.out.println(sb.toString());
    }
}
