from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path("get/", views.delet_user, name="script")
]