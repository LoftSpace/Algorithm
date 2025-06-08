import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        
        // 전체 종류 개수 구하기 
        HashMap<String, Integer> map = new HashMap<>();
        for(String next : gems){
            map.put(next , 0);
        }
        
        int kind = map.keySet().size(); // 전체 종류 
        int cur_kind = 0;               // 현재 종류 
        int start = 0;                  // 현재 시작 좌표 
        int end   = 0;                  // 현재 끝 좌표 
        int size  = gems.length;        // 잼 개수 
        int min   = Integer.MAX_VALUE;  // 최소 구간 거리 
        int min_start = 0;              // 최소 구간 시작 좌표 
        int min_end   = 0;              // 최소 구간 끝 좌표 
        
        // 투포인터 알고리즘 
        while(start <= end){
            if(cur_kind < kind && end == size) break;
            if(cur_kind < kind){
                map.put(gems[end], map.get(gems[end]) + 1);
                if(map.get(gems[end++]) == 1) cur_kind++;
            }
            else{
                map.put(gems[start], map.get(gems[start]) - 1);
                if(map.get(gems[start++]) == 0) cur_kind--;
            }
            // 갱신 
            if(cur_kind == kind){
                if(min > end - start + 1){
                    min = end - start + 1;
                    min_start = start + 1;
                    min_end   = end;
                }
                else if(min == end - start + 1 && start + 1 < min_start){
                    min_start = start + 1;
                    min_end   = end;
                }
            }  
        }
        return new int [] {min_start, min_end};
    }
}