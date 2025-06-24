import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> largeQueue = new PriorityQueue<>();
        PriorityQueue<Integer> smallQueue = new PriorityQueue<>((o1,o2) -> o2 - o1);
        int N = Integer.parseInt(st.nextToken());
        int pointer = 0;
        //init
        st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        pointer = num;
        System.out.println(pointer);

        for(int i = 1; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken());

            if(i %2 == 0){
                if(num > pointer){
                    smallQueue.add(pointer);
                    largeQueue.add(num);
                    pointer = largeQueue.poll();
                }
                else {
                    smallQueue.add(num);
                }
            }
            //홀수개인 상태에서 들어오면
            else {
                if(num > pointer){
                    largeQueue.add(num);
                }
                else {
                    largeQueue.add(pointer);
                    smallQueue.add(num);
                    pointer = smallQueue.poll();
                }
            }
            System.out.println(pointer);
        }
    }
}