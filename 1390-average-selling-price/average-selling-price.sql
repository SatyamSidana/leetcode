# Write your MySQL query statement below
select p.product_id , ifnull(round((sum(p.price*u.units))/sum(u.units),2),0) as average_price from Prices p left join UnitsSold u on p.start_date<=u.purchase_date 
and u.purchase_date<=p.end_date and u.product_id=p.product_id group by p.product_id
