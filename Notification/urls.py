from django.conf.urls import url
from Notification import views

app_name = 'Notification'

urlpatterns = [

    url(r'^Fac/(?P<fac_id>[0-9]+)/$' , views.FacHome , name="FacHome"),
    url(r'^Fac/(?P<fac_id>[0-9]+)/create$' , views.create_notif , name="create"),
    url(r'^Stu/(?P<stu_id>[0-9]+)/$' , views.StuHome , name="StuHome"),
    url(r'^Stu/(?P<stu_id>[0-9]+)/show/$' , views.show_stu_notif , name="show_stu"),

]