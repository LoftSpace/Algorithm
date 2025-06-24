import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Long> pq= new PriorityQueue<>();
        int N = Integer.parseInt(st.nextToken());
        long ans = 0;

        for(int i = 0; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            pq.add(Long.parseLong(st.nextToken()));
        }

        while(pq.size() >= 2){
            long a = pq.poll();
            long b = pq.poll();
            ans += (a + b);
            pq.add(a + b);
        }

        if(N == 1)
            System.out.println(0);
        else
            System.out.println(ans);
    }
}