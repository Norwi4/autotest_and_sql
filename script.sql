/// 1

select c.login, count(o.id) as orders_count 
from "Couriers" c
join "Orders" o on c.id = o."courierId" 
where o."inDelivery" = true
group by c.login;


/// 2

select track, case 
    when finished = true then 2
    when cancelled = true then -1
    when "inDelivery" = true then 1
    else 0
end as status
from "Orders";
