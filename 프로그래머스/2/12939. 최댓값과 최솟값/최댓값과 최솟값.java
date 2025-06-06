class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        int Max = Integer.MIN_VALUE;
        int Min = Integer.MAX_VALUE;
        for(String str : arr){
            int num = Integer.parseInt(str);
            if(num > Max)
                Max = num;
            if (num < Min)
                Min = num;
        }
        String answer = Min + " " + Max;
        return answer;
    }
}