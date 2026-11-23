SELECT order_id, order_date, amount
FROM {{ source('raw', 'orders') }}
