from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from product.models import *
from django.db.models import Count


# Create your views here.


# class HomeView(View):
#     def get(self, request):
#         cateparent = Category.objects.filter(parent_ID=0)
#         allvariation = Variation.objects.all()
#         onSale = Variation.objects.filter(sale_price__lt=600)
#         allproduct = Product.objects.all()
#         vari_id = allvariation.values('id')
#
#         context = {
#             'parents': cateparent,
#             'variations': allvariation,
#             'a': vari_id,
#             'sales': onSale
#         }
#         return render(request, 'homepage/index.html', context)

class HomeView(ListView):
    model = Variation
    paginate_by = 9
    template_name = "homepage/index.html"


class ItemDetailView(DetailView):
    model = Variation
    template_name = "homepage/product.html"
