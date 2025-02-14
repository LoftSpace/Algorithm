import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int S;
    static long answer;
    static long[] tree;
    static ArrayList<Element> elements;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = 1;
        answer = 0;
        while(S < N){
            S *= 2;
        }
        tree = new long[S * 2];
        Arrays.fill(tree,0);
        elements = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< N; i ++){
            elements.add(new Element(Integer.parseInt(st.nextToken()),i));
        }

        Collections.sort(elements);

        for(Element element : elements){
            int num = element.num;
            int index = element.index;
            answer += query(1,S,index,N,1);
            update(1,S,index,1,1);
        }
        System.out.println(answer);
    }
    static long query(int left, int right, int queryLeft, int queryRight, int node){
        if(right < queryLeft || queryRight < left){
            return 0;
        }else if(queryLeft <= left && right <= queryRight){
            return tree[node];
        }else {
            int mid = (left + right) / 2;
            return query(left,mid,queryLeft,queryRight,node * 2) + query(mid + 1,right, queryLeft, queryRight, node * 2 + 1);
        }
    }

    static void update(int left, int right, int target, int node, int diff){
        if(target < left || target > right){
            return;
        }
        tree[node] += diff;
        if(left != right){
            int mid = (left + right) / 2;
            update(left,mid,target,node * 2,diff);
            update(mid + 1,right,target,node * 2 + 1,diff);
        }
    }
}

class Element implements Comparable<Element>{
    int num;
    int index;
    public Element(int num, int index){
        this.num = num;
        this.index = index;
    }

    @Override
    public int compareTo(Element o){
        return this.num - o.num;
    }
}
