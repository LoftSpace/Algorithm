from collections import deque
def solution(n, t, m, timetable):
    def time_to_int(time):
        return int(time[3:]) + int(time[:2]) * 60
    def int_to_time(number):
        time = ''
        hour = number // 60
        if hour < 10 :
            time += '0'
        time += str(hour)
        time += ':'
        minute = number % 60
        if minute < 10 :
            time += '0'
        time += str(minute)
        return time
    
    answer = ''
    people = []
    timetable.sort() 
    timetable_queue = deque(timetable)
    waiting_people = deque([])
    
    #각 버스에 대해
    for bus_num in range(n):
        bus_time = int_to_time(time_to_int("09:00") + (bus_num) * t)
        # 이 버스 도착 이전에 온 사람들
        while timetable_queue and timetable_queue[0] <= bus_time :
            waiting_people.append(timetable_queue.popleft())
        count = 0
        #버스에 태운다
        if bus_num != n - 1 :
            while waiting_people and count < m :
                waiting_people.popleft()
                count += 1
    #print(waiting_people)
    
    # 마지막 버스때 체크
    if len(waiting_people) < m :
        answer = bus_time
    else :
        answer = int_to_time(time_to_int(waiting_people[m - 1]) - 1)
    
    return answer