from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('photo/<int:photo_id>',views.details,name='details'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('about', views.about, name='about'),
    path('concerts', views.concerts, name='concerts'),
    path('contacts', views.contacts, name='contacts'),
]
