import java.util.*;
class Solution {
    public int solution(int[] a) {
        int answer = 0;
        int N = a.length;
        if(N == 1) return 0;
        
        Map<Integer,Integer> map = new HashMap<>();
        
        // 1. 각 원소들의 개수를 센다
        for(int i = 0; i < N; i++){
            if(!map.containsKey(a[i]))
                map.put(a[i],1);
            else 
                map.put(a[i],map.get(a[i]) + 1);
        }
        if(map.keySet().size() == 1) return 0;
        
        for(Integer key : map.keySet()){
            if(map.get(key) <= answer) continue;
            int count = 0;
            
            for(int i = 0; i < N - 1; i++){
                if(a[i] != key && a[i + 1] != key) continue;
                if(a[i] == a[i + 1]) continue;
                count++;
                i++;
            }
            answer = Math.max(answer,count);
        }
        
        return answer * 2;
    }
}