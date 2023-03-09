from django.urls import path
from .import views
urlpatterns=[
    path("req/",views.my_form,name="req"),
] 