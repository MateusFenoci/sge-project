from django.urls import path
from . import views

urlpatterns = [
    path('sizes/list/', views.SizeListView.as_view(), name='size_list'),
    path('sizes/create/', views.SizeCreateView.as_view(), name='size_create'),
    path('sizes/<int:pk>/detail/', views.SizeDetailView.as_view(), name='size_detail'),
    path('sizes/<int:pk>/update/', views.SizeUpdateView.as_view(), name='size_update'),
    path('sizes/<int:pk>/delete/', views.SizeDeleteView.as_view(), name='size_delete'),

    path('api/v1/sizes/', views.SizeCreateListAPIView.as_view(), name='size-create-list-api-view'),
    path('api/v1/sizes/<int:pk>/', views.SizeRetrieveUpdateDestroyAPIView.as_view(), name='size-detail-api-view'),
]
