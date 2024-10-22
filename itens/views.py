from django.shortcuts import render, get_object_or_404

# Create your views here.
# itens/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from products.models import Product
from itens.models import Item
from rest_framework.views import APIView
from itens.serializers import ItemSerializer



class ItemListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    paginate_by = 10
    permission_required = 'itens.view_item'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        size = self.request.GET.get('size')

        if product:
            queryset = queryset.filter(product__id=product)
        if size:
            queryset = queryset.filter(size__icontains=size)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Item
    template_name = 'item_create.html'
    form_class = forms.ItemForm
    success_url = reverse_lazy('item_list')
    permission_required = 'itens.add_item'


class ItemDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Item
    template_name = 'item_detail.html'
    permission_required = 'itens.view_item'


class ItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Item
    template_name = 'item_update.html'
    form_class = forms.ItemForm
    success_url = reverse_lazy('item_list')
    permission_required = 'itens.change_item'


class ItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('item_list')
    permission_required = 'itens.delete_item'


class ItemCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class ProductItemsAPIView(generics.GenericAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        return Item.objects.filter(product=product)

    def get(self, request, *args, **kwargs):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)