-- This script displays the average temperatures by city ordered by
-- temperatures descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
