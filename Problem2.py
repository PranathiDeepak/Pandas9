import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].nunique().reset_index()
    orders_sorted = orders.sort_values('order_number', ascending = False).head(1)
    return orders_sorted[['customer_number']]