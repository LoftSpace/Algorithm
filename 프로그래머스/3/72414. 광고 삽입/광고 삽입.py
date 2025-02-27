def solution(play_time, adv_time, logs):
    def time_to_int(time):
        hour,min,sec = time.split(":")
        return int(hour) * 3600 + int(min) * 60 + int(sec)
    def int_to_time(num):
        time = ''
        hour = num // 3600
        if hour < 10:
            time += '0'
        time += str(hour)
        time += ':'
        
        num %= 3600
        min = num // 60
        if min < 10 :
            time += '0'
        time += str(min)
        time += ':'
        
        num %= 60
        sec = num
        if num < 10 :
            time += '0'
        time += str(sec)
        return time
    
    
    answer = ''
    Max = 0
    play_time_int = time_to_int(play_time)
    
    intersect_arr = [0] * (play_time_int + 2)
    adv_time_int = time_to_int(adv_time)
    print(play_time_int)
    if adv_time_int == play_time_int :
        return "00:00:00"
    for log in logs:
        start_s, end_s = log.split('-')
        start,end = time_to_int(start_s),time_to_int(end_s)
        intersect_arr[start] += 1
        intersect_arr[end] -= 1
    
    
    for i in range(1,play_time_int + 2):
        intersect_arr[i] = intersect_arr[i] + intersect_arr[i-1]
    for i in range(1,play_time_int + 2):
        intersect_arr[i] = intersect_arr[i] + intersect_arr[i-1]
    
    Max = 0
    
    for i in range(adv_time_int - 1,play_time_int):
        if i == adv_time_int - 1:
            if Max < intersect_arr[i] : 
                answer = int_to_time(i - adv_time_int + 1)
                Max = intersect_arr[i]
        else :
            if Max < intersect_arr[i] - intersect_arr[i-adv_time_int]:
                answer = int_to_time(i - adv_time_int + 1)
                Max = intersect_arr[i] - intersect_arr[i-adv_time_int]
        
  
    return answer