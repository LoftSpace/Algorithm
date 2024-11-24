import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static long[] LIS;
	static long[] input;
	static int N;
	static int lastIndex=0;
	static long[] trace;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		Stack<Long> stack = new Stack<>();
		
		N = Integer.parseInt(st.nextToken());
		LIS = new long[N];
		input = new long[N];
		trace =  new long[N];
		st = new StringTokenizer(br.readLine());
		
		for(int i=0;i<N;i++)
			input[i] = Long.parseLong(st.nextToken());
		
		LIS[0] = input[0];
		
		
		for(int i=0;i<N;i++) {
			if(input[i] > LIS[lastIndex]) {
				LIS[++lastIndex] = input[i];
				trace[i] = lastIndex; 
			} else {
				int k = lowerBound(lastIndex,input[i]);
				LIS[k] = input[i];
				trace[i] = k; 
			}
		}
		System.out.println(lastIndex+1);
	
		
		for(int i=N-1;i>=0;i--) {
			if(trace[i] == lastIndex) {
				//System.out.print(input[i]);
				stack.push(input[i]);
				lastIndex--;
			}
		}
		while(!stack.isEmpty()) {
			System.out.print(stack.pop()+" ");
		}
	}
	static int lowerBound(int lastIndex, long input) {
		int mid;
		int left = 0;
		int right = lastIndex;
		while(left < right) {
			mid = (left + right)/2;
			if(LIS[mid] < input) {
				left=  mid+1;
			} else {
				right = mid;
			}
		}
		return right;
	}

}