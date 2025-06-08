import java.util.*;
import java.io.*;

class Solution {
    static int[] tree;
    public int solution(int n, int[][] costs) {
        int answer = 0;
        tree = new int[n];
        for(int i = 0; i <n; i++)
            tree[i] = i;
        PriorityQueue<Bridge> pq = new PriorityQueue<>((b1,b2) -> b1.cost - b2.cost);
        for(int[] cost : costs){
            pq.add(new Bridge(cost[0],cost[1],cost[2]));
        }
        while(!pq.isEmpty()){
            Bridge bridge = pq.poll();
            int u = bridge.u;
            int v = bridge.v;
            if(find(u) == find(v)) continue;
            
            union(u,v);
            answer += bridge.cost;
        }
        
        
        return answer;
    }
    static void union(int a, int b){
        int aRoot = find(a);
        int bRoot = find(b);
        tree[aRoot] = bRoot;
    }
    
    static int find(int a){
        if(a != tree[a])
            tree[a] = find(tree[a]);
        return tree[a];
    }
}
class Bridge {
    int u;
    int v;
    int cost;
    
    public Bridge(int u, int v, int cost){
        this.u = u;
        this.v = v;
        this.cost = cost;
    }
}