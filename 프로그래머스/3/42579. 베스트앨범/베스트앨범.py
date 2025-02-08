import heapq
def solution(genres, plays):
    hash = dict()
    hash2 = dict()
    genre_sort = []
    answer = []
    for index,genre in enumerate(genres):
        if genre in hash :
            hash[genre] += plays[index]
            heapq.heappush(hash2[genre],[-plays[index],index])
        else :
            hash[genre] = plays[index]
            hash2[genre] = []
            heapq.heapify(hash2[genre])
            heapq.heappush(hash2[genre],[-plays[index],index])
            
   
    for i in hash:
        genre_sort.append([hash[i],i])
    genre_sort.sort(reverse = True)
    for i in genre_sort:
        curr_genre = i[1]
        curr_musics = hash2[curr_genre]
        if len(curr_musics) == 1 :
            answer.append(heapq.heappop(curr_musics)[1])
        else :
            answer.append(heapq.heappop(curr_musics)[1])
            answer.append(heapq.heappop(curr_musics)[1])
    return answer