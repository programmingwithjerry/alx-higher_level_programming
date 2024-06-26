-- displays the max temperature of each state (ordered by State name)
SELECT `state`, max(value) as `maximum_temperature`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
