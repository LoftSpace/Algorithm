import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;



public class Main {
	static int N,M;
	static int numOfEdges;
	static int selectedEdge=0;
	static Point[][] grid;
	static boolean[][] visited;
	static int islandNum=1;
	static int[] set;
	static int[][] fromTo;
	static int[] dRow = {-1,1,0,0};
	static int[] dCol = {0,0,-1,1};
	static Edge[] graph;
	static int totalCost=0;
	static boolean[] connect;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int type;
		grid = new Point[N][M];
		visited = new boolean[N][M];
		
		for(int row=0;row<N;row++) {
			st = new StringTokenizer(br.readLine());
			for(int col=0; col<M;col++) {
				type = Integer.parseInt(st.nextToken());
				grid[row][col] = new Point(row,col,type);
				visited[row][col] = false;
			}
		}
		//섬 정의 확인
				
		//dfs  -> 섬 정의 O(n^2)
		for(int row=0;row<N;row++) { 
			for(int col=0;col<M;col++) {
				if(!visited[row][col] && grid[row][col].type==1) { //새로운 섬 발견
					dfs(row,col);
					islandNum++;
				}
			}
		}
		//섬 정의 확인
		/*
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++)
				System.out.print(grid[i][j].island + " ");
			System.out.println();
		}
		*/
		fromTo = new int[islandNum+1][islandNum+1];
		set = new int[islandNum+1];
		graph = new Edge[islandNum+1];
		connect = new boolean[islandNum+1];
		
		for(int i=1; i<islandNum+1; i++)
			for(int j=1; j<islandNum+1; j++) 
				fromTo[i][j]=100;
		
		//각 점 돌면서 최소거리 갱신 O(n^2)
		for(int row=0;row<N;row++) {
			for(int col=0; col<M; col++) {
				if(grid[row][col].type==1) {
					searchNorth(row,col,grid[row][col].island);
					searchSouth(row,col,grid[row][col].island);
					searchEast(row,col,grid[row][col].island);
					searchWest(row,col,grid[row][col].island);
				}
			}
		}
		
		
		
		 numOfEdges=0;
		
		
		//edge 정보는 fromTo 배열에 있다.
		//크루스칼 알고리즘 O(nlogn)
		
		//그래프 생성
		for(int i=1; i<islandNum; i++) { //#i번 섬 
			for(int j=1; j<islandNum; j++) {
					if(fromTo[i][j] !=100) { //다리를 그래프에 넣는다
						//System.out.println(i+"->"+j+":"+fromTo[i][j]);
						numOfEdges++;
					}
			}
		}
		graph = new Edge[numOfEdges];
		int k=0;
		for(int i=1; i<islandNum; i++) { //#i번 섬 
			for(int j=1; j<islandNum; j++) {
				
					if(fromTo[i][j] !=100) { //다리를 그래프에 넣는다
						graph[k] = new Edge(i,j,fromTo[i][j]);
					
						k++;
					}
			}
		}
		
		Arrays.sort(graph, new Comparator<Edge>() {
            @Override
            public int compare(Edge o1, Edge o2) {
                return o1.cost-o2.cost;
            }
        });
		
		init();
		kruskal();
		//System.out.print(selectedEdge);
		//System.out.print(islandNum);
		if(selectedEdge < islandNum-2)
			System.out.print(-1);
		else
			System.out.print(totalCost);
		
	}

	static void dfs(int row,int col) {
		//
		visited[row][col] = true;
		
		grid[row][col].island = islandNum;
		
		for(int dir=0;dir<4;dir++) {
			int nextRow = row + dRow[dir] ;
			int nextCol = col + dCol[dir];
			
			if(0<=nextRow && nextRow<N && 0<=nextCol && nextCol < M  ) 
				if(!visited[nextRow][nextCol])
					if(grid[nextRow][nextCol].type==1)
						dfs(nextRow,nextCol);
				
		}
	}
	
	static void searchNorth(int row,int col,int startIsland) {
		int nextRow = row;
		int nextCol = col; //탐색하는 노드가 땅이고 같은 섬이 아닐 때 까지
		boolean found=false;
		//시작 섬과 다른 섬에 도착 + 땅 
		while(nextRow>0) {
			nextRow--;
			if(grid[nextRow][nextCol].island== startIsland )
				break;
			if(grid[nextRow][nextCol].type==1 && grid[nextRow][nextCol].island != startIsland && grid[nextRow][nextCol].island !=0) {
				found=true;
				//System.out.println("found" + startIsland + "to"+ grid[nextRow][nextCol].island+"and cost is" + (row-nextRow));
				break;
			}
			
		}
		
		int cost = row-nextRow-1;
		int from = startIsland;
		int to = grid[nextRow][nextCol].island;
	
		//간선 업데이트 
		if(found && cost >1) {// 다음 섬을 찾았고 거리가 1보다 크다 
			//다리의 길이가 최소다
			if(fromTo[from][to] > cost ) {
			
				fromTo[grid[row][col].island][grid[nextRow][nextCol].island] = cost;
			}
		}
			
	}
	static void searchSouth(int row,int col,int startIsland) {
		int nextRow = row;
		int nextCol = col; //탐색하는 노드가 땅이고 같은 섬이 아닐 때 까지
		boolean found=false;
		while(nextRow<N-1) {
			nextRow++;
			if(grid[nextRow][nextCol].island== startIsland )
				break;
			if(grid[nextRow][nextCol].type==1 && grid[nextRow][nextCol].island != startIsland && grid[nextRow][nextCol].island !=0) {
				found=true;
				break;
			}
			
		}
		int cost = nextRow-row-1;
		int from =  startIsland;
		int to = grid[nextRow][nextCol].island;
		//간선 업데이트 
		if(found && cost >1) {
			if(fromTo[from][to] > cost) {
				fromTo[grid[row][col].island][grid[nextRow][nextCol].island] = cost;
				
			}
		}
}
	static void searchEast(int row,int col,int startIsland) {
		int nextRow = row;
		int nextCol = col; //탐색하는 노드가 땅이고 같은 섬이 아닐 때 까지
		boolean found = false;
		while(nextCol<M-1) {
			nextCol++;
			if(grid[nextRow][nextCol].island== startIsland )
				break;
			if(grid[nextRow][nextCol].type==1 && grid[nextRow][nextCol].island != startIsland&& grid[nextRow][nextCol].island !=0) {
				found=true;
				break;
			}
			
		}
		int cost = nextCol-col-1;
		int from =  startIsland;
		int to = grid[nextRow][nextCol].island;
		//간선 업데이트 
		if(found && cost>1)
			if(fromTo[from][to] > cost) {
				fromTo[grid[row][col].island][grid[nextRow][nextCol].island] = cost;
				
			}
	}
	static void searchWest(int row,int col,int startIsland) {
		int nextRow = row;
		int nextCol = col; //탐색하는 노드가 땅이고 같은 섬이 아닐 때 까지
		boolean found = false;
		while(nextCol>0) {
			nextCol--;
			if(grid[nextRow][nextCol].island== startIsland )
				break;
			if(grid[nextRow][nextCol].type==1 && grid[nextRow][nextCol].island != startIsland&& grid[nextRow][nextCol].island !=0) {
				found=true;
				break;
			}
			
		}
		int cost = col-nextCol-1;
		int from = startIsland;
		int to = grid[nextRow][nextCol].island;
		//간선 업데이트 
		if(found && cost>1)
			if(fromTo[from][to] > cost)
				fromTo[grid[row][col].island][grid[nextRow][nextCol].island] = cost;
	
	}
		
	
	static void kruskal() {
		
		
		for(int i=1;i<numOfEdges;i++)
		{	
			if(find(graph[i].from)==find(graph[i].to))
				continue;
			
			union(graph[i].from,graph[i].to);
			selectedEdge++;
			totalCost+= graph[i].cost;
			
			
			if(selectedEdge==islandNum-1) {
				break;
			}
			
			
		}
		
			
	}
	static void init() {
		for(int i=0;i<islandNum+1;i++)
			set[i]=i;
	}
	static void union(int a,int b) { //섬 a vs 섬 b
		int aRoot = find(a);
		int bRoot = find(b);
		if(aRoot != bRoot)
			set[aRoot] = bRoot;
	}
	static int find(int a) {
		if(set[a]==a)
			return a;
		return set[a] = find(set[a]);
		
	}
}
class Point {
	int row;
	int col;
	int type;
	int island;
	public Point(int row, int col,int type) {
		
		this.type = type;
		this.row = row;
		this.col = col;
	}
	
}
class Edge {
	int from;
	int to;
	int cost;
	public Edge(int from, int to, int cost) {
	
		this.from = from;
		this.to = to;
		this.cost = cost;
	}
	
}
