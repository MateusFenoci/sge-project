from django.urls import path
from . import views

urlpatterns = [
    path('itens/list/', views.ItemListView.as_view(), name='item_list'),
    path('itens/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('itens/<int:pk>/detail/', views.ItemDetailView.as_view(), name='item_detail'),
    path('itens/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('itens/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),

    path('api/v1/itens/', views.ItemCreateListAPIView.as_view(), name='item-create-list-api-view'),
    path('api/v1/itens/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail-api-view'),
    path('api/products/<int:product_id>/items/', views.ProductItemsAPIView.as_view(), name='product-items'),
]
