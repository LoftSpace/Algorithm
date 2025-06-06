import java.io.*;
import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        Map<Integer,Integer> map = new HashMap<>();
        for(int t : tangerine){
            if(map.containsKey(t)){
                int before = map.get(t);
                map.replace(t,before,before + 1);
            }
            else
                map.put(t,1);
        }
        
        List<Integer> arr = new ArrayList<>(map.values());
        arr.sort(Collections.reverseOrder());
        
        for(int count : arr){
            answer++;
            k -= count;
            if(k <= 0)
                return answer;
        }
        return answer;
    }
}