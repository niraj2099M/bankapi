from django.urls import path
from . import views

urlpatterns = [
    path('banks', views.BankList.as_view(), name="banklist"),
    path('branch', views.branch_details, name="branch"),

]

