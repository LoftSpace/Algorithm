import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int N = jobs.length;
        int answer = 0;
        PriorityQueue<Job> pq = new PriorityQueue<>();
        List<Job> queue = new LinkedList<>();
        
        for(int i = 0; i< N; i++)
            queue.add(new Job(i,jobs[i][1],jobs[i][0]));
            
        Collections.sort(queue,(o1,o2) -> o1.requestTime - o2.requestTime);
        
        
        int time = 0;
        while(!queue.isEmpty() || !pq.isEmpty()){
            //작업 큐에 들어올 수 있는 작업들
            while(!queue.isEmpty() && queue.get(0).requestTime <= time){
                Job job = queue.remove(0);
                pq.add(job);
                
            }
            
            if(!pq.isEmpty()){
                Job job = pq.poll();
                if(time < job.requestTime)
                    time = job.requestTime;
                
                
                time += job.duration;
                answer += (time - job.requestTime);
            }
            else if(!queue.isEmpty()){
                time = queue.get(0).requestTime;
            }
        }
        
        
        return answer / N;
    }
}
class Job implements Comparable<Job>{
    int num;
    int duration;
    int requestTime;
    
    public Job(int num, int duration, int requestTime){
        this.num = num;
        this.duration = duration;
        this.requestTime = requestTime;
    }
    
    @Override
    public int compareTo(Job o){
        if(this.duration == o.duration){
            if(this.requestTime == o.requestTime){
                return this.num = o.num;
            }
            else return this.requestTime - o.requestTime;
        }
        else return this.duration - o.duration;
    }
    
}