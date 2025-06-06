class Solution {
    public int solution(int n) {
        
        
        int count = Integer.toBinaryString(n).replace("0","").length();
        
        while(true){
            n ++;
            if(Integer.toBinaryString(n).replace("0","").length() == count)
                return n;
        }    
    }
    
    static String toBinary(int n){
        
        StringBuilder sb = new StringBuilder();
        while(n > 0){
            sb.append(n % 2);
            n /= 2;
        }
        return sb.reverse().toString();
    }
    
    static int countOne(String a){
        int count = 0;
        for(int i = 0; i < a.length(); i ++)
            if(a.charAt(i) == '1')
                count ++;
        return count;
    }
}