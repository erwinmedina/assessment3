from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('addwish/', views.WishCreate.as_view(), name='add_wish'),
    path('delete/<int:wish_id>/', views.delete_wish, name='delete_wish')
]