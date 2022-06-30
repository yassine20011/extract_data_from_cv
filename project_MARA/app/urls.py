from . import views
from django.urls import path

urlpatterns = [
    path('', views.UploadView.as_view() ,name='index'),
] 