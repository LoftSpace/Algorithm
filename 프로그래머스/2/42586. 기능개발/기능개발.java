import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int time = 0;
        int count = 0;
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        
        for(int i = 0; i < progresses.length; i++)
            queue.add(i);
        
        while(!queue.isEmpty()){System.out.println(time);
            int index = queue.poll();
            int progress = progresses[index];
            progress += time * speeds[index];
            
            if(progress >= 100)
                count++;  
            else {
                time += Math.ceil((100 - progress) / speeds[index]);
                if((100 - progress) % speeds[index] != 0)
                    time++;
                
                if(index != 0) 
                    list.add(count);
                    
                count = 1;
            }
        }
        list.add(count);
        
        answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++)
            answer[i] = list.get(i);
        return answer;
    }
}