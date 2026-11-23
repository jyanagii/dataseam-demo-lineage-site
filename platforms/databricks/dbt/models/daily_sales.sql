SELECT order_date, SUM(amount) AS total_amount
FROM {{ ref('orders') }}
GROUP BY 1
