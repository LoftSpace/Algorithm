import java.util.*;
import java.io.*;
class Solution {
    public int solution(int[][] maps) {
        int[] dRow = {1,-1,0,0};
        int[] dCol = {0,0,1,-1};
        int answer = 0;
        int N = maps.length;
        int M = maps[0].length;
        boolean[][] visited = new boolean[N][M];
        Queue<Node> queue = new LinkedList<>();
        
        queue.add(new Node(0,0,1));
        
        while(!queue.isEmpty()){
            Node currentNode = queue.poll();
            int currentRow = currentNode.row;
            int currentCol = currentNode.col;
            int move = currentNode.move;
            
            if(currentRow == N - 1 && currentCol == M -1)
                return move;
            
            for(int dir = 0; dir < 4; dir++){
                int nextRow = currentRow + dRow[dir];
                int nextCol = currentCol + dCol[dir];
                
                if(0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < M && !visited[nextRow][nextCol] && maps[nextRow][nextCol] != 0){
                    queue.add(new Node(nextRow,nextCol,move + 1));
                    visited[nextRow][nextCol] = true;
                }
                
            }
        }
        return -1;
    }
}
class Node{
    int row;
    int col;
    int move;
    public Node(int row,int col, int move){
        this.row = row;
        this.col = col;
        this.move = move;
    }
}