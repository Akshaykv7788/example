from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create,name='create'),
    path('show/',views.show,name='show'),
    path('delete/<id>',views.delete,name='delete'),
    path('update/<id>',views.update,name='update'),
    path('',views.show)
]