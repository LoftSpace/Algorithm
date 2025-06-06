import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        
        int N = plays.length;
        PriorityQueue<Genre> genreQueue = new PriorityQueue<>((o1,o2) -> o2.totalPlay - o1.totalPlay);
        Map<String,PriorityQueue<Music>> map = new HashMap<>();
        Map<String,Integer> genreMap = new HashMap<>();
        
        for(int i = 0; i < plays.length;i++){
            String genre = genres[i];
            int play = plays[i];
            
            if(map.containsKey(genre)){
                int temp = genreMap.get(genre);
                genreMap.put(genre,temp + play);
                map.get(genre).add(new Music(i,play));
            }
            else {
                genreMap.put(genre,play);
                map.put(genre,new PriorityQueue<>());
                map.get(genre).add(new Music(i,play));
            }
        }
        
        for(String key : genreMap.keySet()){
            genreQueue.add(new Genre(key,genreMap.get(key)));
        }
        
        int j = 0;
        List<Integer> ans = new ArrayList<>();
        //각 장르에 대해
        while(!genreQueue.isEmpty()){
            Genre genre = genreQueue.poll();
            
            PriorityQueue<Music> musicQueue = map.get(genre.genre);
            
            
            for(int i = 0; i < 2; i ++){
                if(musicQueue.isEmpty())
                    break;
                
                ans.add(musicQueue.poll().num);
            }
            
        
        }
        answer = new int[ans.size()];
        int index = 0;
        for(Integer i : ans){
            answer[index] = i;
            index++;
                
        }
        
        
        return answer;
    }
}
class Music implements Comparable<Music>{
    int num;
    int plays;
    
    public Music(int num, int plays){
        this.num = num;
        this.plays = plays;
    }
    
    @Override
    public int compareTo(Music o2){
        if(this.plays == o2.plays){
            return this.num - o2.num;
        }
        return o2.plays - this.plays;
    }
}

class Genre implements Comparable<Genre> {
    String genre;
    int totalPlay;
    
    public Genre(String genre, int totalPlay){
        this.genre = genre;
        this.totalPlay = totalPlay;
    }
    
    @Override
    public int compareTo(Genre o2){
        return o2.totalPlay - this.totalPlay;
    }
        
}