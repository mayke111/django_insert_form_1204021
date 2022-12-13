from django.urls import path

from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('addpost/', views.form_post, name='add post')
]
