import java.util.*;
import java.io.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String,List<String>> hash = new HashMap<>();
        
        for(String[] cloth : clothes){
            if(hash.containsKey(cloth[1]))
                hash.get(cloth[1]).add(cloth[0]);
            else{
                hash.put(cloth[1],new ArrayList<>());
                hash.get(cloth[1]).add(cloth[0]);
            }
        }
        
        for(String key : hash.keySet()){
            answer *= (hash.get(key).size() + 1);
        }
        
        return answer - 1;
    }
}