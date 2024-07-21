# Write your MySQL query statement below
select W1.id  from Weather W1 left join Weather W2 on W1.recordDate=W2.recordDate + interval 1 day where 
W1.temperature > W2.temperature
