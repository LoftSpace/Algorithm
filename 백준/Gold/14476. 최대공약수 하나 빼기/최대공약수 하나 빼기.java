import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] leftGcd;
	static int[] rightGcd;
	static int[] num;
	static int N;
	static int max=-1;
	static int save=-1;
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		num = new int[N];
		leftGcd = new int[N];
		rightGcd = new int[N];
		
		st = new StringTokenizer(br.readLine());
		
		for(int i=0;i<N;i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}
		
		leftGcd[0] = num[0];
		leftGcd[1] = gcd(num[0],num[1]);
		rightGcd[N-1] = num[N-1];
		rightGcd[N-2] = gcd(num[N-1],num[N-2]);
		
		for(int i=2 ;i<N;i++) {
			leftGcd[i] = gcd(leftGcd[i-1],num[i]);
			rightGcd[N-i-1] = gcd(rightGcd[N-i],num[N-i-1]);
		}
		
		//System.out.println(Arrays.toString(leftGcd));
		//System.out.println(Arrays.toString(rightGcd));
		if(num[N-1]%leftGcd[N-2]!=0) {
			if(leftGcd[N-2] > max) {
				max = leftGcd[N-2];
				save = num[N-1];
			}
		}
		
		if(num[0]%rightGcd[1]!=0) {
			if(rightGcd[1] > max) {
				max = rightGcd[1];
				save = num[0];
			}
		}
		
		for(int i=0 ;i <=N-3;i++) {
			int temp = gcd(leftGcd[i],rightGcd[i+2]);
			if(num[i+1]%temp!=0) {
				if(temp > max) {
					max = temp;
					save = num[i+1];
				}
			}
			
		}
		System.out.println(max);
		if(max!=-1)
			System.out.println(save);
		
	}
	//gcd(a ,b) = gcd(b, b%a)
	static int gcd(int a,int b) {
		while(b != 0) {
			int r = a % b;
			a = b;
			b = r;
		}
		return a;
	}


}