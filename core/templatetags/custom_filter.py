from django import template
from product.models import Category, Variation

register = template.Library()


@register.filter
def getChilds(parentID):
    return Category.objects.filter(parent_ID=parentID)


# @register.filter
# def hasChilds(parentID):
#     childs = Category.objects.filter(parent_ID=parentID)
#     # return childs is not None
#     if (childs is not None):
#         return True
#     return False


def sale(sale_price, price):
    return (price - sale_price) * 100 / price


@register.filter
def hasSale(Saleid):
    sale_price = Variation.objects.filter(id=Saleid).values('sale_price')
    sale_price_value = sale_price[0].values()
    price = Variation.objects.filter(id=Saleid).values('price')
    price_value = price[0].values()
    a = (price_value - sale_price_value)
    return a
