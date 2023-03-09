from django.urls import path
from .import views
urlpatterns=[
    path("",views.signup,name="signup"),
    path("index/",views.index,name="index"),

    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("newbooks/",views.newbooks,name="newbooks"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("signin/",views.signin,name="logout"),
    
    
    
]