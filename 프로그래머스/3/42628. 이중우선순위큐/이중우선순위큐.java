import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> b - a);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> a - b);
        Map<Integer,Boolean> hash = new HashMap<>();
        
        //각 연산에 대해
        for(String operation : operations){
            String[] ops = operation.split(" ");
           // System.out.println(ops[0]);
            //삽입
            if(ops[0].equals("I")){
                maxHeap.add(Integer.parseInt(ops[1]));
                minHeap.add(Integer.parseInt(ops[1]));
                hash.put(Integer.parseInt(ops[1]),true);
                //System.out.println(ops[1] + "삽입");
            }
            //삭제
            else{
                if(ops[1].equals("-1")){
                    while(!minHeap.isEmpty()){
                        int num = minHeap.poll();
                        if(hash.get(num) == true){
                            hash.put(num,false);
                            break;
                        }
                    }
                }
                else{
                    while(!maxHeap.isEmpty()){
                        int num = maxHeap.poll();
                        if(hash.get(num) == true){
                            hash.put(num,false);
                            //System.out.println(num + "삭제");
                            break;
                        }
                    }
                }
            }
        }
        
        answer = new int[2];
        List<Integer> arr = new ArrayList<>();
        
        for(Integer num : hash.keySet()){
            if(hash.get(num) == true)
                arr.add(num);
        }
        if(arr.isEmpty()){
            answer[0] = 0;
            answer[1] = 0;
            return answer;
        }
            
        Collections.sort(arr);
        
        answer[0] = arr.get(arr.size() - 1);
        answer[1] = arr.get(0);
        
        return answer;
    }
}