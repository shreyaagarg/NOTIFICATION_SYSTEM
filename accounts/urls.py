from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url( r'StuSignUp/$' , views.StuSignUpView , name="StuSignUp"),
    url( r'logout/$' , views.Proflogout, name="logout"),
    url( r'StuLogIn/$', views.StuLogInView , name="StuLogIn"),
    url( r'FacLogIn/$', views.FacLogInView , name="FacLogIn"),
    url( r'FacSignUp/$' , views.FacSignUpView , name="FacSignUp"),
    url(r'select/$', views.select,name="select")
]