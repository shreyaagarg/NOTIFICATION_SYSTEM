from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from Notification import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , TemplateView.as_view(template_name='index.html') , name="index"),
    url(r'^about/$' , TemplateView.as_view(template_name='about.html') , name="about"),
    url(r'^contact/$' , TemplateView.as_view(template_name='contact.html') , name="contact"),
    url(r'accounts/', include('accounts.urls')),
    url(r'home/', include('Notification.urls')),
    url(r'notifications', views.NotifList.as_view()),
]