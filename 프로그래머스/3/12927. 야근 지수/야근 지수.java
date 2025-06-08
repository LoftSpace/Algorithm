import java.util.*;
import java.io.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        for(int work : works)
            pq.add(work);
        while(!pq.isEmpty() && n > 0){
            int num = pq.poll();
            num--;
            n--;
            if(num > 0)
                pq.add(num);
        }
        
        while(!pq.isEmpty()){
            int num = pq.poll();
            answer += (num * num);
        }
        
        return answer;
    }
}