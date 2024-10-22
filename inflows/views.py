# inflows/views.py

from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from itens.models import Item
from suppliers.models import Supplier

class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        item = self.request.GET.get('item')
        supplier = self.request.GET.get('supplier')

        if item:
            queryset = queryset.filter(item__id=item)
        if supplier:
            queryset = queryset.filter(supplier__id=supplier)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InflowUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Inflow
    template_name = 'inflow_update.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.change_inflow'


class InflowDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Inflow
    template_name = 'inflow_delete.html'
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.delete_inflow'


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
