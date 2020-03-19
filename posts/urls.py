from django.urls import path,include
from .views import *

app_name = 'post'

urlpatterns = [
    path('',post_index),
    path('index/',post_index,name='index'),
     path('create/',post_create,name='create'),

    path('<slug:slug>',post_detail,name='detail'),

   # path('<int:id>/',post_detail,name='detail'),
    
    path('<slug:slug>/update/',post_update,name='update'),
    path('<slug:slug>/delete/',post_delete,name='delete'),


]
