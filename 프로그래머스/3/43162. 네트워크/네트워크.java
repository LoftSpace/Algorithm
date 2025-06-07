import java.io.*;
import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        //각 노드 돌면서
        for(int startNode = 0; startNode < n; startNode++){
            if(visited[startNode]) continue;
            // 탐색 안된 노드에서 시작
            
            answer++;
            queue.add(startNode);
            visited[startNode] = true;
            while(!queue.isEmpty()){
                int node = queue.poll();
                
                //해당 노드에서 연결된 노드 탐색
                for(int col = 0; col < n; col++)
                {
                    //방문 아직 안한 노드면 큐에 삽입
                    if(computers[node][col] == 1 && !visited[col] )
                    {   
                        
                        queue.add(col);
                        visited[col] = true;
                    }
                }
            }
        }
        return answer;
    }
}