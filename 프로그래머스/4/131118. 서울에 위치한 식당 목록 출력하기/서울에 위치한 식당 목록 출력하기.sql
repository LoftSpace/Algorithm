-- 코드를 입력하세요
with T1 as (select rest_id,round(avg(review_score),2) as review_score
from REST_REVIEW
where rest_id in (select rest_id from REST_INFO where address like "서울%")
group by rest_id)

select R.rest_id,R.rest_name,R.food_type,R.favorites,R.address,T1.review_score
from REST_INFO R
join T1 on R.rest_id = T1.rest_id
order by T1.review_score desc, favorites desc