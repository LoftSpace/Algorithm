-- 코드를 입력하세요
select car_id,P.car_type,round(daily_fee * 30 * (100 - discount_rate) * 0.01,0) as FEE
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
Join 
    (select car_id, daily_fee,car_type
     from CAR_RENTAL_COMPANY_CAR C
     where C.car_id not in 
            (SELECT car_id
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
            where H.START_DATE <= '2022-11-30' and H.END_DATE >= '2022-11-01')
            and 
            (C.car_type = '세단' or C.car_type = 'SUV')
 ) as T2 on 
 T2.car_type = P.car_type 
 where P.duration_type = '30일 이상' 
 Having FEE >= 500000 and FEE < 2000000
 order by FEE desc, P.car_type asc,car_id desc