from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from product.models import *
from cart.models import *
from django.db.models import Count


# Create your views here.

class HomeView(ListView):
    model = Variation
    paginate_by = 9
    template_name = "homepage/index.html"


class ItemDetailView(DetailView):
    model = Variation
    template_name = "homepage/product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Variation, slug=slug)
    order_item, created = CartItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
