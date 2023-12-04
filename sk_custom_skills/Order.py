import semantic_kernel as sk
from semantic_kernel.skill_definition import sk_function
import datetime

class Order:
    @sk_function(
        description="Returns today's date",
        name="current_date",
    )
    def current_date(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    @sk_function(
        description="Get order delivery status and date",
        name="get_order_status",
        input_description="order id"
    )
    def get_order_status(self, order_id:str) -> str:
        if order_id == '1':
            order = {'item_name':'A', 'order_date':'2023-10-10', 'delivery_status':'completed', 'delivery_date':'2023-10-11'}
        if order_id == '2':
            order = {'item_name':'B', 'order_date':'2023-11-22', 'delivery_status':'completed', 'delivery_date':'2023-11-23'}
        if order_id == '3':
            order = {'item_name':'C', 'order_date':'2023-12-01', 'delivery_status':'in delivery', 'delivery_date':'2023-12-15'}
        return str(order) 