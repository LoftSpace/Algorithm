class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int N = sequence.length;
        long[] arr1 = new long[N];
        
        long[] arrSum = new long[N + 1];
        
        for(int i = 0; i < N; i++){
            if(i%2 == 0)
                arr1[i] = sequence[i] * (-1);
            else 
                arr1[i] = sequence[i];
        }
        
        arrSum[0] = 0;
        arrSum[1] = arr1[0];
        
        for(int i = 1; i < N; i++)
            arrSum[i + 1] = arr1[i] + arrSum[i];
        
        
        long Max = Long.MIN_VALUE;
        long Min = Long.MAX_VALUE;
        
        
        for(int i = 0; i < N + 1; i++){
            if(arrSum[i] > Max)
                Max = arrSum[i];
            if(arrSum[i] < Min)
                Min = arrSum[i];
        }
        
        answer = Max - Min;
        return answer;
    }
}