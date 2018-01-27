from django.urls import path
from . import views

app_name = 'inspiration'

urlpatterns = [
    # /inspiration
    path('', views.InspirationView.as_view(), name="index"),
    # /inspiration/5/
    path('<int:pk>/', views.DetailView.as_view(), name="detail")

]