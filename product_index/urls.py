from django.urls import path
from product_index import views

urlpatterns = [
    path('apps/', views.AppList.as_view(), name='api-app-list'),
    path('app/<int:pk>', views.AppDetail.as_view(), name='api-app')
]
