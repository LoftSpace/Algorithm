-- 코드를 작성해주세요
select T2.id as Id, T3.fish_name as FISH_NAME, T1.length as LENGTH
from FISH_INFO  T2
join (
    select fish_type,max(f.length) as length
    from FISH_INFO f
    group by f.fish_type
    ) as T1
on T1.length = T2.length and T1.fish_type = T2.fish_type
join FISH_NAME_INFO as T3 on T1.fish_type = T3.fish_type 

