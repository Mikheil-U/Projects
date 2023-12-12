from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login_user'),
    path('logout/', views.user_logout, name='logout_user'),
    path('delete-movie/<int:pk>', views.delete_table_item_on_click, name='delete_movie'),

]
