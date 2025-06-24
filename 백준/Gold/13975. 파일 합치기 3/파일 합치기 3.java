import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for(int tc = 0; tc < T; tc++){
            long ans = 0;
            PriorityQueue<Long> pq = new PriorityQueue<>();
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());

            for(int i = 0; i < N; i++){
                pq.add(Long.parseLong(st.nextToken()));
            }

            while(pq.size() >= 2){
                long a = pq.poll();
                long b = pq.poll();
                pq.add(a + b);
                ans += (a + b);
            }

            System.out.println(ans);
        }
    }
}