import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] locations;
    static int[] gaps;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        locations = new int[N];
        gaps = new int[N + 1];
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; i++)
            locations[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(locations);
        if(N != 0) {
            gaps[0] = locations[0];

            for (int i = 0; i < N - 1; i++)
                gaps[i + 1] = locations[i + 1] - locations[i];
            gaps[N] = L - locations[N - 1];
        }
        else {
            gaps[0] = L;
        }

        int left = 1;
        int right = L;

        while(left <= right){
            int mid = (left + right) / 2;
            int needs = func(mid);

            // mid 거리만큼 만들기 위해 M개보다 더 많이 필요할때 (목표값을 더 낮춰야 함)
            if(needs > M)
                left = mid + 1;
            //충분하다
            else if(needs < M)
                right = mid - 1;
            else
                right = mid - 1;
        }
        System.out.println(left);

    }

    static int func(int m){
        int result = 0;
        for(int i = 0; i < N + 1; i ++){
            if(gaps[i] > m) {
                result += Math.floorDiv(gaps[i], m);
                if (gaps[i] % m == 0)
                    result--;
            }
        }
        return result;
    }
}