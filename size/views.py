from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class SizeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Size
    template_name = 'size_list.html'
    context_object_name = 'sizes'
    paginate_by = 10
    permission_required = 'sizes.view_size'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SizeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Size
    template_name = 'size_create.html'
    form_class = forms.SizeForm
    success_url = reverse_lazy('size_list')
    permission_required = 'sizes.add_size'


class SizeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Size
    template_name = 'size_detail.html'
    permission_required = 'sizes.view_size'


class SizeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Size
    template_name = 'size_update.html'
    form_class = forms.SizeForm
    success_url = reverse_lazy('size_list')
    permission_required = 'sizes.change_size'


class SizeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Size
    template_name = 'size_delete.html'
    success_url = reverse_lazy('size_list')
    permission_required = 'sizes.delete_size'


class SizeCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer


class SizeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
