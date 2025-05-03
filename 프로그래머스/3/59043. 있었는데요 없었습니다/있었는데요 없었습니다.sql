-- 코드를 입력하세요
SELECT I.animal_id, I.name
from ANIMAL_INS I
join ANIMAL_OUTS O on I.animal_id = O.animal_id
where I.datetime > O.datetime
order by I.datetime
