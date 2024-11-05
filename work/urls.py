from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.work_create,name='createproduct'),
        path('retrieve/',views.work_read,name='retrieveproduct'),
        path('update/<int:id>/',views.work_update,name='updateproduct'),
        path('delete/<int:pk>',views.work_delete,name='deleteproduct'),
       
    ]