-- 코드를 작성해주세요
with T1 as (select parent_id as id,count(*) as child_num
from ECOLI_DATA
group by parent_id)

select E.ID,IFNULL(child_num,0) as CHILD_COUNT
from ECOLI_DATA E
left join T1 on E.id = T1.id