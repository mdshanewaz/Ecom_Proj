from django import template
from Order_App.models import OrderModel


register = template.Library()

@register.filter()
def cart_total(user):
    order = OrderModel.objects.filter(user=user, ordered=False)
    if order.exists():
        
        print("Order item") 
        print(order[0].orderitems.count())
        return order[0].orderitems.count()
    else:
        return 0
    