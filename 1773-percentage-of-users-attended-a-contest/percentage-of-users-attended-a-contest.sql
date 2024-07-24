SELECT contest_id,
       ROUND(COUNT(contest_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id order by percentage desc ,contest_id