from django.urls import path
from .views import post, blog

urlpatterns = [
    path('', blog, name='post-list'),
    path('<int:id>', post, name='post-detail')
]