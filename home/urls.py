from django.urls import path,include
from .views import *

app_name = 'home'

urlpatterns = [
    path('',home_index),
    path('index/',home_index,name='home'),
   	#path('create/',post_create,name='create'),

    path('<slug:slug>/detail/',home_detail,name='detail'),


   # path('<int:id>/',post_detail,name='detail'),
    
    path('<slug:slug>/update/',home_update,name='update'),
    path('<slug:slug>/delete/',home_delete,name='delete'),


]
